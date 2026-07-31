"""Small local server for the IceCream HTML prototype.

Run from the repository root with:
    python prototype/server.py
"""

from __future__ import annotations

import base64
import binascii
import csv
import hashlib
import hmac
import json
import os
import re
import secrets
from collections import Counter
from datetime import datetime, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock
from urllib.parse import parse_qs, urlparse


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
WIREFRAME_DIR = REPOSITORY_ROOT / "prototype" / "wireframe"
LANDING_PAGE_DIR = REPOSITORY_ROOT / "landing-page"
USERS_FILE = REPOSITORY_ROOT / "data" / "Users_records.csv"
ARTWORKS_FILE = REPOSITORY_ROOT / "data" / "artworks_records.csv"
COMMENTS_FILE = REPOSITORY_ROOT / "data" / "comments_records.csv"
UPLOADS_DIR = WIREFRAME_DIR / "uploads"
CSV_FIELDS = ("User_id", "Nickname", "Password", "Gender")
ARTWORK_FIELDS = (
    "Art_id",
    "User_id",
    "Title",
    "Description",
    "Image_URLs",
    "Tags",
    "View_Count",
    "Like_Count",
    "Comment_Count",
    "Sanity_Level",
    "Status",
    "Created_At",
    "Updated_At",
    "Deleted_At",
)
COMMENT_FIELDS = ("Comments_id", "Art_id", "User_id", "Content", "Status")
USERS_LOCK = Lock()
ARTWORKS_LOCK = Lock()
COMMENTS_LOCK = Lock()
ALLOWED_IMAGE_TYPES = {
    "image/jpeg": (".jpg", b"\xff\xd8\xff"),
    "image/png": (".png", b"\x89PNG\r\n\x1a\n"),
    "image/gif": (".gif", b"GIF8"),
}
MAX_IMAGE_SIZE = 10 * 1024 * 1024
MAX_IMAGES = 5


class AuthenticationRequiredError(Exception):
    """Raised when a protected prototype action has no valid signed-in user."""


def next_user_id(rows: list[dict[str, str]]) -> str:
    numbers = []
    for row in rows:
        match = re.fullmatch(r"U(\d+)", row.get("User_id", ""))
        if match:
            numbers.append(int(match.group(1)))
    return f"U{max(numbers, default=0) + 1:03d}"


def next_art_id(rows: list[dict[str, str]]) -> str:
    numbers = []
    for row in rows:
        match = re.fullmatch(r"A(\d+)", row.get("Art_id", ""))
        if match:
            numbers.append(int(match.group(1)))
    return f"A{max(numbers, default=0) + 1:03d}"


def next_comment_id(rows: list[dict[str, str]]) -> str:
    numbers = []
    for row in rows:
        match = re.fullmatch(r"C(\d+)", row.get("Comments_id", ""))
        if match:
            numbers.append(int(match.group(1)))
    return f"C{max(numbers, default=0) + 1:03d}"


def user_exists(user_id: str) -> bool:
    if not USERS_FILE.exists():
        return False
    with USERS_LOCK:
        with USERS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                raise RuntimeError("Users_records.csv has an unexpected header.")
            return any(row["User_id"] == user_id for row in reader)


def get_nickname(user_id: str) -> str:
    if not USERS_FILE.exists():
        return user_id
    with USERS_LOCK:
        with USERS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                raise RuntimeError("Users_records.csv has an unexpected header.")
            for row in reader:
                if row["User_id"] == user_id:
                    return row["Nickname"]
    return user_id


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
    return f"pbkdf2_sha256$200000${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored_password: str) -> bool:
    try:
        algorithm, iterations_text, salt_text, expected_text = stored_password.split(
            "$", 3
        )
        if algorithm != "pbkdf2_sha256":
            return False
        iterations = int(iterations_text)
        if iterations < 1 or iterations > 1_000_000:
            return False
        salt = bytes.fromhex(salt_text)
        expected = bytes.fromhex(expected_text)
    except (TypeError, ValueError):
        return False

    actual = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iterations
    )
    return hmac.compare_digest(actual, expected)


def authenticate_user(nickname: str, password: str) -> dict[str, str] | None:
    nickname = nickname.strip()
    if not nickname or not password or not USERS_FILE.exists():
        return None

    with USERS_LOCK:
        with USERS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                raise RuntimeError("Users_records.csv has an unexpected header.")
            for row in reader:
                if (
                    row["Nickname"].casefold() == nickname.casefold()
                    and verify_password(password, row["Password"])
                ):
                    return {"user_id": row["User_id"], "nickname": row["Nickname"]}
    return None


def register_user(nickname: str, password: str, gender: str) -> str:
    nickname = nickname.strip()
    if not 2 <= len(nickname) <= 30:
        raise ValueError("Nickname must contain between 2 and 30 characters.")
    if any(character in nickname for character in "\r\n"):
        raise ValueError("Nickname cannot contain line breaks.")
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")
    if any(character in password for character in "\r\n"):
        raise ValueError("Password cannot contain line breaks.")

    with USERS_LOCK:
        USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
        rows: list[dict[str, str]] = []
        if USERS_FILE.exists():
            with USERS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                    raise RuntimeError("Users_records.csv has an unexpected header.")
                rows = list(reader)

        if any(row["Nickname"].casefold() == nickname.casefold() for row in rows):
            raise ValueError("This nickname is already registered.")

        user_id = next_user_id(rows)
        write_header = not USERS_FILE.exists() or USERS_FILE.stat().st_size == 0
        with USERS_FILE.open("a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            if write_header:
                writer.writeheader()
            writer.writerow(
                {
                    "User_id": user_id,
                    "Nickname": nickname,
                    "Password": hash_password(password),
                    "Gender": gender,
                }
            )
        return user_id


def decode_image(image: object) -> tuple[str, bytes]:
    if not isinstance(image, dict):
        raise ValueError("Each uploaded image must be a valid file.")
    mime_type = image.get("type")
    encoded_data = image.get("data")
    if mime_type not in ALLOWED_IMAGE_TYPES or not isinstance(encoded_data, str):
        raise ValueError("Only JPEG, PNG, and GIF images are accepted.")
    try:
        content = base64.b64decode(encoded_data, validate=True)
    except (ValueError, binascii.Error) as error:
        raise ValueError("An uploaded image contains invalid data.") from error
    if not content or len(content) > MAX_IMAGE_SIZE:
        raise ValueError("Each image must be between 1 byte and 10 MB.")
    extension, signature = ALLOWED_IMAGE_TYPES[mime_type]
    if not content.startswith(signature):
        raise ValueError("An uploaded file does not match its image type.")
    return extension, content


def create_artwork(payload: dict[str, object]) -> str:
    user_id = payload.get("user_id")
    title = payload.get("title")
    description = payload.get("description", "")
    tags = payload.get("tags")
    sanity_level = payload.get("sanity_level")
    images = payload.get("images")

    if not isinstance(user_id, str) or not user_exists(user_id):
        raise AuthenticationRequiredError("Please sign in before uploading artwork.")
    if not isinstance(title, str) or not 1 <= len(title.strip()) <= 100:
        raise ValueError("Title must contain between 1 and 100 characters.")
    if not isinstance(description, str) or len(description) > 2_000:
        raise ValueError("Description cannot exceed 2,000 characters.")
    if not isinstance(tags, list) or not 1 <= len(tags) <= 10:
        raise ValueError("Add between 1 and 10 tags.")
    clean_tags = []
    for tag in tags:
        if not isinstance(tag, str):
            raise ValueError("Tags must be text.")
        clean_tag = tag.strip().lower()
        if not clean_tag or len(clean_tag) > 30 or "|" in clean_tag:
            raise ValueError("Each tag must contain 1 to 30 characters.")
        if clean_tag not in clean_tags:
            clean_tags.append(clean_tag)
    if not clean_tags:
        raise ValueError("Add at least one tag.")
    if sanity_level not in (0, 18, 19):
        raise ValueError("Select a valid age limit.")
    if not isinstance(images, list) or not 1 <= len(images) <= MAX_IMAGES:
        raise ValueError(f"Upload between 1 and {MAX_IMAGES} images.")

    decoded_images = [decode_image(image) for image in images]
    with ARTWORKS_LOCK:
        rows: list[dict[str, str]] = []
        if ARTWORKS_FILE.exists():
            with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                    raise RuntimeError("artworks_records.csv has an unexpected header.")
                rows = list(reader)

        art_id = next_art_id(rows)
        UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
        saved_paths: list[Path] = []
        image_urls: list[str] = []
        try:
            for index, (extension, content) in enumerate(decoded_images, start=1):
                filename = f"{art_id.lower()}-{index}-{secrets.token_hex(4)}{extension}"
                destination = UPLOADS_DIR / filename
                destination.write_bytes(content)
                saved_paths.append(destination)
                image_urls.append(f"/uploads/{filename}")

            now = datetime.now(timezone.utc).isoformat(timespec="seconds")
            write_header = (
                not ARTWORKS_FILE.exists() or ARTWORKS_FILE.stat().st_size == 0
            )
            with ARTWORKS_FILE.open("a", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=ARTWORK_FIELDS)
                if write_header:
                    writer.writeheader()
                writer.writerow(
                    {
                        "Art_id": art_id,
                        "User_id": user_id,
                        "Title": title.strip(),
                        "Description": description.strip(),
                        "Image_URLs": json.dumps(image_urls),
                        "Tags": "|".join(clean_tags),
                        "View_Count": "0",
                        "Like_Count": "0",
                        "Comment_Count": "0",
                        "Sanity_Level": str(sanity_level),
                        "Status": "Published",
                        "Created_At": now,
                        "Updated_At": now,
                        "Deleted_At": "",
                    }
                )
        except Exception:
            for saved_path in saved_paths:
                saved_path.unlink(missing_ok=True)
            raise
    return art_id


def get_user_artworks(user_id: str) -> list[dict[str, object]]:
    if not user_exists(user_id):
        raise ValueError("User not found.")
    if not ARTWORKS_FILE.exists():
        return []

    artworks: list[dict[str, object]] = []
    with ARTWORKS_LOCK:
        with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                raise RuntimeError("artworks_records.csv has an unexpected header.")
            for row in reader:
                if row["User_id"] != user_id or row["Deleted_At"]:
                    continue
                try:
                    image_urls = json.loads(row["Image_URLs"])
                except json.JSONDecodeError:
                    image_urls = []
                if not isinstance(image_urls, list):
                    image_urls = []
                artworks.append(
                    {
                        "art_id": row["Art_id"],
                        "title": row["Title"],
                        "description": row["Description"],
                        "image_urls": [
                            url for url in image_urls if isinstance(url, str)
                        ],
                        "tags": [tag for tag in row["Tags"].split("|") if tag],
                        "view_count": int(row["View_Count"] or 0),
                        "like_count": int(row["Like_Count"] or 0),
                        "comment_count": int(row["Comment_Count"] or 0),
                        "sanity_level": int(row["Sanity_Level"] or 0),
                        "status": row["Status"],
                        "created_at": row["Created_At"],
                    }
                )
    return artworks


def get_artwork(
    art_id: str, increment_view: bool = False
) -> dict[str, object] | None:
    if not ARTWORKS_FILE.exists():
        return None
    with ARTWORKS_LOCK:
        with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                raise RuntimeError("artworks_records.csv has an unexpected header.")
            rows = list(reader)

        row = next(
            (
                candidate
                for candidate in rows
                if candidate["Art_id"] == art_id and not candidate["Deleted_At"]
            ),
            None,
        )
        if row is None:
            return None

        if increment_view:
            row["View_Count"] = str(int(row["View_Count"] or 0) + 1)
            row["Updated_At"] = datetime.now(timezone.utc).isoformat(
                timespec="seconds"
            )
            temporary_file = ARTWORKS_FILE.with_name(
                f".{ARTWORKS_FILE.name}.{secrets.token_hex(4)}.tmp"
            )
            try:
                with temporary_file.open(
                    "w", encoding="utf-8", newline=""
                ) as file:
                    writer = csv.DictWriter(file, fieldnames=ARTWORK_FIELDS)
                    writer.writeheader()
                    writer.writerows(rows)
                temporary_file.replace(ARTWORKS_FILE)
            finally:
                temporary_file.unlink(missing_ok=True)

        try:
            image_urls = json.loads(row["Image_URLs"])
        except json.JSONDecodeError:
            image_urls = []
        return {
            "art_id": row["Art_id"],
            "user_id": row["User_id"],
            "title": row["Title"],
            "description": row["Description"],
            "image_urls": image_urls if isinstance(image_urls, list) else [],
            "tags": [tag for tag in row["Tags"].split("|") if tag],
            "view_count": int(row["View_Count"] or 0),
            "like_count": int(row["Like_Count"] or 0),
            "comment_count": int(row["Comment_Count"] or 0),
            "sanity_level": int(row["Sanity_Level"] or 0),
            "status": row["Status"],
            "created_at": row["Created_At"],
        }
    return None


def get_comments(art_id: str) -> list[dict[str, str]]:
    if get_artwork(art_id) is None:
        raise ValueError("Artwork not found.")
    if not COMMENTS_FILE.exists():
        return []

    with COMMENTS_LOCK:
        with COMMENTS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != COMMENT_FIELDS:
                raise RuntimeError("comments_records.csv has an unexpected header.")
            rows = [
                row
                for row in reader
                if row["Art_id"] == art_id and row["Status"] == "Published"
            ]

    return [
        {
            "comment_id": row["Comments_id"],
            "art_id": row["Art_id"],
            "user_id": row["User_id"],
            "nickname": get_nickname(row["User_id"]),
            "content": row["Content"],
            "status": row["Status"],
        }
        for row in rows
    ]


def create_comment(payload: dict[str, object]) -> dict[str, str]:
    art_id = payload.get("art_id")
    user_id = payload.get("user_id")
    content = payload.get("content")

    if not isinstance(user_id, str) or not user_exists(user_id):
        raise AuthenticationRequiredError("Please sign in before posting a comment.")
    if not isinstance(art_id, str) or get_artwork(art_id) is None:
        raise ValueError("Artwork not found.")
    if not isinstance(content, str):
        raise ValueError("Comment content is required.")
    clean_content = content.strip()
    if not 1 <= len(clean_content) <= 1_000:
        raise ValueError("Comment must contain between 1 and 1,000 characters.")

    with COMMENTS_LOCK:
        COMMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
        rows: list[dict[str, str]] = []
        if COMMENTS_FILE.exists():
            with COMMENTS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                if tuple(reader.fieldnames or ()) != COMMENT_FIELDS:
                    raise RuntimeError("comments_records.csv has an unexpected header.")
                rows = list(reader)

        comment_id = next_comment_id(rows)
        write_header = (
            not COMMENTS_FILE.exists() or COMMENTS_FILE.stat().st_size == 0
        )
        with COMMENTS_FILE.open("a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=COMMENT_FIELDS)
            if write_header:
                writer.writeheader()
            writer.writerow(
                {
                    "Comments_id": comment_id,
                    "Art_id": art_id,
                    "User_id": user_id,
                    "Content": clean_content,
                    "Status": "Published",
                }
            )

    with ARTWORKS_LOCK:
        with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                raise RuntimeError("artworks_records.csv has an unexpected header.")
            artwork_rows = list(reader)
        target = next(
            (
                row
                for row in artwork_rows
                if row["Art_id"] == art_id and not row["Deleted_At"]
            ),
            None,
        )
        if target is not None:
            target["Comment_Count"] = str(int(target["Comment_Count"] or 0) + 1)
            target["Updated_At"] = datetime.now(timezone.utc).isoformat(
                timespec="seconds"
            )
            temporary_file = ARTWORKS_FILE.with_name(
                f".{ARTWORKS_FILE.name}.{secrets.token_hex(4)}.tmp"
            )
            try:
                with temporary_file.open(
                    "w", encoding="utf-8", newline=""
                ) as file:
                    writer = csv.DictWriter(file, fieldnames=ARTWORK_FIELDS)
                    writer.writeheader()
                    writer.writerows(artwork_rows)
                temporary_file.replace(ARTWORKS_FILE)
            finally:
                temporary_file.unlink(missing_ok=True)

    return {
        "comment_id": comment_id,
        "art_id": art_id,
        "user_id": user_id,
        "nickname": get_nickname(user_id),
        "content": clean_content,
        "status": "Published",
    }


def update_artwork(
    art_id: str, user_id: str, action: str, value: object
) -> dict[str, object]:
    if not user_exists(user_id):
        raise AuthenticationRequiredError("Please sign in to continue.")
    with ARTWORKS_LOCK:
        with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                raise RuntimeError("artworks_records.csv has an unexpected header.")
            rows = list(reader)

        target = next(
            (
                row
                for row in rows
                if row["Art_id"] == art_id and not row["Deleted_At"]
            ),
            None,
        )
        if target is None:
            raise ValueError("Artwork not found.")

        response: dict[str, object]
        if action == "like":
            if not isinstance(value, bool):
                raise ValueError("A valid liked state is required.")
            current_count = int(target["Like_Count"] or 0)
            target["Like_Count"] = str(
                current_count + 1 if value else max(0, current_count - 1)
            )
            response = {"like_count": int(target["Like_Count"]), "liked": value}
        elif action == "tag":
            if target["User_id"] != user_id:
                raise AuthenticationRequiredError(
                    "Only the artwork owner can add tags."
                )
            if not isinstance(value, str):
                raise ValueError("A tag is required.")
            tag = value.strip().lower().lstrip("#")
            if not tag or len(tag) > 30 or "|" in tag or "," in tag:
                raise ValueError("A tag must contain between 1 and 30 characters.")
            tags = [existing for existing in target["Tags"].split("|") if existing]
            if tag not in tags:
                if len(tags) >= 10:
                    raise ValueError("An artwork can have at most 10 tags.")
                tags.append(tag)
                target["Tags"] = "|".join(tags)
            response = {"tags": tags}
        else:
            raise ValueError("Unsupported artwork update.")

        target["Updated_At"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        temporary_file = ARTWORKS_FILE.with_name(
            f".{ARTWORKS_FILE.name}.{secrets.token_hex(4)}.tmp"
        )
        try:
            with temporary_file.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=ARTWORK_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            temporary_file.replace(ARTWORKS_FILE)
        finally:
            temporary_file.unlink(missing_ok=True)
        return response


def get_homepage_content() -> dict[str, object]:
    if not ARTWORKS_FILE.exists():
        return {"tags": [], "newest": [], "recommended": []}

    with ARTWORKS_LOCK:
        with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                raise RuntimeError("artworks_records.csv has an unexpected header.")
            rows = [
                row
                for row in reader
                if row["Status"] == "Published" and not row["Deleted_At"]
            ]

    nicknames: dict[str, str] = {}
    if USERS_FILE.exists():
        with USERS_LOCK:
            with USERS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                    raise RuntimeError("Users_records.csv has an unexpected header.")
                nicknames = {
                    row["User_id"]: row["Nickname"]
                    for row in reader
                }

    tag_counts: Counter[str] = Counter()
    cards: list[dict[str, object]] = []
    for row in rows:
        tags = [tag for tag in row["Tags"].split("|") if tag]
        tag_counts.update(tags)
        try:
            image_urls = json.loads(row["Image_URLs"])
        except json.JSONDecodeError:
            image_urls = []
        if not isinstance(image_urls, list) or not image_urls:
            continue
        cards.append(
            {
                "art_id": row["Art_id"],
                "title": row["Title"],
                "image_url": image_urls[0],
                "user_id": row["User_id"],
                "artist_nickname": nicknames.get(row["User_id"], row["User_id"]),
                "like_count": int(row["Like_Count"] or 0),
                "created_at": row["Created_At"],
            }
        )

    newest = sorted(
        cards, key=lambda artwork: str(artwork["created_at"]), reverse=True
    )[:6]
    recommended = list(cards)
    secrets.SystemRandom().shuffle(recommended)
    return {
        "tags": [tag for tag, _count in tag_counts.most_common(10)],
        "newest": newest,
        "recommended": recommended[:10],
    }


def search_artworks(query: str, mode: str) -> list[dict[str, object]]:
    query = query.strip().casefold()
    if not query:
        return []
    if mode not in ("all", "title", "tag"):
        raise ValueError("Search mode must be all, title, or tag.")
    if len(query) > 100:
        raise ValueError("Search text cannot exceed 100 characters.")
    if not ARTWORKS_FILE.exists():
        return []

    with ARTWORKS_LOCK:
        with ARTWORKS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if tuple(reader.fieldnames or ()) != ARTWORK_FIELDS:
                raise RuntimeError("artworks_records.csv has an unexpected header.")
            rows = list(reader)

    nicknames: dict[str, str] = {}
    if USERS_FILE.exists():
        with USERS_LOCK:
            with USERS_FILE.open("r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                if tuple(reader.fieldnames or ()) != CSV_FIELDS:
                    raise RuntimeError("Users_records.csv has an unexpected header.")
                nicknames = {
                    row["User_id"]: row["Nickname"]
                    for row in reader
                }

    results: list[dict[str, object]] = []
    for row in rows:
        if row["Status"] != "Published" or row["Deleted_At"]:
            continue
        tags = [tag for tag in row["Tags"].split("|") if tag]
        title_matches = query in row["Title"].casefold()
        tag_matches = any(query in tag.casefold() for tag in tags)
        if not (
            (mode == "all" and (title_matches or tag_matches))
            or (mode == "title" and title_matches)
            or (mode == "tag" and tag_matches)
        ):
            continue
        try:
            image_urls = json.loads(row["Image_URLs"])
        except json.JSONDecodeError:
            image_urls = []
        if not isinstance(image_urls, list) or not image_urls:
            continue
        results.append(
            {
                "art_id": row["Art_id"],
                "title": row["Title"],
                "image_url": image_urls[0],
                "tags": tags,
                "user_id": row["User_id"],
                "artist_nickname": nicknames.get(row["User_id"], row["User_id"]),
                "like_count": int(row["Like_Count"] or 0),
                "created_at": row["Created_At"],
            }
        )
    return sorted(
        results, key=lambda artwork: str(artwork["created_at"]), reverse=True
    )[:50]


class PrototypeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WIREFRAME_DIR), **kwargs)

    def translate_path(self, path: str) -> str:
        request_path = urlparse(path).path
        if request_path == "/landing-page":
            return str(LANDING_PAGE_DIR)
        if request_path.startswith("/landing-page/"):
            relative_path = request_path.removeprefix("/landing-page/").strip("/")
            candidate = (LANDING_PAGE_DIR / relative_path).resolve()
            landing_root = LANDING_PAGE_DIR.resolve()
            if candidate == landing_root or landing_root in candidate.parents:
                return str(candidate)
            return str(landing_root / "__not_found__")
        return super().translate_path(path)

    def do_GET(self) -> None:
        parsed_url = urlparse(self.path)
        if parsed_url.path == "/api/comments":
            try:
                art_id = parse_qs(parsed_url.query).get("art_id", [""])[0]
                if not art_id:
                    raise ValueError("An art_id query parameter is required.")
                comments = get_comments(art_id)
                self.send_json(
                    200, {"comments": comments, "comment_count": len(comments)}
                )
            except ValueError as error:
                self.send_json(400, {"error": str(error)})
            except RuntimeError as error:
                self.send_json(500, {"error": str(error)})
            except OSError:
                self.send_json(500, {"error": "Unable to read comment records."})
            return
        if parsed_url.path == "/api/search":
            try:
                parameters = parse_qs(parsed_url.query)
                query = parameters.get("q", [""])[0]
                mode = parameters.get("mode", ["all"])[0]
                self.send_json(
                    200,
                    {
                        "query": query,
                        "mode": mode,
                        "results": search_artworks(query, mode),
                    },
                )
            except ValueError as error:
                self.send_json(400, {"error": str(error)})
            except RuntimeError as error:
                self.send_json(500, {"error": str(error)})
            except OSError:
                self.send_json(500, {"error": "Unable to read artwork records."})
            return
        if parsed_url.path == "/api/homepage":
            try:
                self.send_json(200, get_homepage_content())
            except RuntimeError as error:
                self.send_json(500, {"error": str(error)})
            except OSError:
                self.send_json(500, {"error": "Unable to read homepage data."})
            return
        if parsed_url.path == "/api/artworks":
            try:
                user_id = parse_qs(parsed_url.query).get("user_id", [""])[0]
                if not user_id:
                    raise ValueError("A user_id query parameter is required.")
                self.send_json(200, {"artworks": get_user_artworks(user_id)})
            except ValueError as error:
                self.send_json(400, {"error": str(error)})
            except RuntimeError as error:
                self.send_json(500, {"error": str(error)})
            except OSError:
                self.send_json(500, {"error": "Unable to read artwork records."})
            return
        artwork_match = re.fullmatch(r"/api/artworks/(A\d+)", parsed_url.path)
        if artwork_match:
            try:
                artwork = get_artwork(
                    artwork_match.group(1), increment_view=True
                )
                if artwork is None:
                    self.send_json(404, {"error": "Artwork not found."})
                else:
                    artwork["artist_nickname"] = get_nickname(
                        str(artwork["user_id"])
                    )
                    self.send_json(200, artwork)
            except RuntimeError as error:
                self.send_json(500, {"error": str(error)})
            except OSError:
                self.send_json(500, {"error": "Unable to read artwork records."})
            return
        if parsed_url.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", "/Sign-Up.html")
            self.end_headers()
            return
        super().do_GET()

    def do_POST(self) -> None:
        if self.path not in (
            "/api/signup",
            "/api/login",
            "/api/artworks",
            "/api/artworks/like",
            "/api/artworks/tags",
            "/api/comments",
        ):
            self.send_error(404)
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            maximum_size = 70_000_000 if self.path == "/api/artworks" else 10_000
            if content_length <= 0 or content_length > maximum_size:
                raise ValueError("Invalid request size.")
            payload = json.loads(self.rfile.read(content_length))
            if not isinstance(payload, dict):
                raise ValueError("Invalid request body.")
            if self.path in ("/api/artworks/like", "/api/artworks/tags"):
                action = "like" if self.path.endswith("/like") else "tag"
                value = payload.get("liked") if action == "like" else payload.get("tag")
                result = update_artwork(
                    str(payload.get("art_id", "")),
                    str(payload.get("user_id", "")),
                    action,
                    value,
                )
                self.send_json(200, result)
                return
            if self.path == "/api/comments":
                comment = create_comment(payload)
                self.send_json(201, comment)
                return
            if self.path == "/api/artworks":
                art_id = create_artwork(payload)
                self.send_json(201, {"art_id": art_id})
                return

            nickname = payload.get("nickname")
            password = payload.get("password")
            gender = payload.get("gender")
            if not isinstance(nickname, str) or not isinstance(password, str):
                raise ValueError("Nickname and password are required.")
            if self.path == "/api/signup":
                user_id = register_user(nickname, password, gender)
                self.send_json(201, {"user_id": user_id})
            else:
                user = authenticate_user(nickname, password)
                if user is None:
                    self.send_json(401, {"error": "Invalid nickname or password."})
                else:
                    self.send_json(200, user)
        except AuthenticationRequiredError as error:
            self.send_json(401, {"error": str(error)})
        except (ValueError, json.JSONDecodeError) as error:
            self.send_json(400, {"error": str(error)})
        except RuntimeError as error:
            self.send_json(500, {"error": str(error)})
        except OSError:
            self.send_json(
                500,
                {
                    "error": (
                        "Unable to save the file. Close the CSV in Excel and try again."
                    )
                },
            )

    def send_json(self, status: int, payload: dict[str, object]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("ICECREAM_PORT", "8000"))
    server = ThreadingHTTPServer(("127.0.0.1", port), PrototypeHandler)
    print(f"IceCream prototype: http://127.0.0.1:{port}/Sign-Up.html")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
