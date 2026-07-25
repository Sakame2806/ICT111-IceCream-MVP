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

> This CSV approach is suitable only for the local classroom prototype. A
> production application should use a database with proper access controls.
