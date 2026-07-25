"""Small local server for the IceCream HTML prototype.

Run from the repository root with:
    python prototype/server.py
"""

from __future__ import annotations

import csv
import hashlib
import hmac
import json
import re
import secrets
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Lock


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
WIREFRAME_DIR = REPOSITORY_ROOT / "prototype" / "wireframe"
USERS_FILE = REPOSITORY_ROOT / "data" / "Users_records.csv"
CSV_FIELDS = ("User_id", "Nickname", "Password")
USERS_LOCK = Lock()


def next_user_id(rows: list[dict[str, str]]) -> str:
    numbers = []
    for row in rows:
        match = re.fullmatch(r"U(\d+)", row.get("User_id", ""))
        if match:
            numbers.append(int(match.group(1)))
    return f"U{max(numbers, default=0) + 1:03d}"


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


def register_user(nickname: str, password: str) -> str:
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
                }
            )
        return user_id


class PrototypeHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WIREFRAME_DIR), **kwargs)

    def do_GET(self) -> None:
        if self.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", "/Sign-Up.html")
            self.end_headers()
            return
        super().do_GET()

    def do_POST(self) -> None:
        if self.path not in ("/api/signup", "/api/login"):
            self.send_error(404)
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length <= 0 or content_length > 10_000:
                raise ValueError("Invalid request size.")
            payload = json.loads(self.rfile.read(content_length))
            if not isinstance(payload, dict):
                raise ValueError("Invalid request body.")
            nickname = payload.get("nickname")
            password = payload.get("password")
            if not isinstance(nickname, str) or not isinstance(password, str):
                raise ValueError("Nickname and password are required.")
            if self.path == "/api/signup":
                user_id = register_user(nickname, password)
                self.send_json(201, {"user_id": user_id})
            else:
                user = authenticate_user(nickname, password)
                if user is None:
                    self.send_json(401, {"error": "Invalid nickname or password."})
                else:
                    self.send_json(200, user)
        except (ValueError, json.JSONDecodeError) as error:
            self.send_json(400, {"error": str(error)})
        except RuntimeError as error:
            self.send_json(500, {"error": str(error)})

    def send_json(self, status: int, payload: dict[str, str]) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), PrototypeHandler)
    print("IceCream prototype: http://127.0.0.1:8000/Sign-Up.html")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
