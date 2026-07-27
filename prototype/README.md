# IceCream interactive prototype

Start the local server from the repository root:

```powershell
python prototype/server.py
```

Then open <http://127.0.0.1:8000/Sign-Up.html>.

The sign-up form validates the entered data, rejects duplicate nicknames, assigns
the next available `U###` user ID, and appends the account to
`data/Users_records.csv`. Passwords are stored as salted PBKDF2-SHA256 hashes in
the existing `Password` column rather than as readable plain text.

Registered users can sign in at <http://127.0.0.1:8000/login.html>. The login
service reads the same CSV file, verifies the password hash, and returns the
matching user ID and nickname. After a successful login, the page stores this
basic identity in browser session storage and opens the user dashboard.

Signed-in users can upload artwork at <http://127.0.0.1:8000/Upload.html>.
JPEG, PNG, and GIF files are saved under `prototype/wireframe/uploads/`, while
their artwork metadata is appended to `data/artworks_records.csv`. The prototype
accepts up to five images of 10 MB each per artwork.

The profile gallery loads every non-deleted image belonging to the current user
from `data/artworks_records.csv`. Clicking the top-right avatar opens an account
menu. Signed-in users can open
their profile or select `Logout`, which clears the browser session and returns
to the login page. Signed-out users see a `Login` menu item.

Selecting an item in the profile gallery opens
`Artwork.html?art_id=<artwork-id>`. The detail page renders multi-image works in
upload order from top to bottom. Signed-in users can like or unlike a work, and
the artwork owner can add tags; both changes update `artworks_records.csv`.
Comments are display-only placeholders in the current prototype.

`homepage.html` loads its content from `/api/homepage`. It displays up to 10
tags ranked by use frequency, up to 6 newest published works ordered by
`Created_At`, and up to 10 randomly ordered recommendations. Homepage cards
open the corresponding artwork detail page.

The shared top navigation search opens `Search.html` when Enter is pressed.
`/api/search` supports case-insensitive partial matching against artwork titles,
tags, or both. Search results include only published, non-deleted works with an
available image and link to their artwork detail pages.

> This CSV approach is suitable only for the local classroom prototype. A
> production application should use a database with proper access controls.

online database supabase  https://supabase.com/dashboard/project/sncdfgkzwewdtqzovnlh
