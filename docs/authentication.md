# Authentication

Users can register and log in. Notes belong to a user, and each user can only
see, change and delete their own notes.

## How It Works

```text
1. POST /auth/register   username + password  → user is saved
2. POST /auth/login      username + password  → API returns a token
3. GET  /notes           Authorization: Bearer <token>  → only your notes
```

- **Passwords are hashed with Argon2.** The database only stores the hash, so
  even someone who reads the `users` table cannot see the passwords.
- **The token is a JWT.** It contains the user id and an expiry time (60
  minutes) and is signed with `SECRET_KEY`. If anyone changes the token, the
  signature no longer matches and the API rejects it.
- **Ownership is checked on every request.** Asking for another user's note
  returns `404 Not Found`, so the API doesn't even reveal that it exists.

## Endpoints

| Method | Path | Login needed | Description |
| --- | --- | --- | --- |
| `POST` | `/auth/register` | No | Create a user |
| `POST` | `/auth/login` | No | Get a token |
| `GET` | `/auth/me` | Yes | Show the logged-in user |
| `GET`/`POST` | `/notes` | Yes | List or create your notes |
| `GET`/`PUT`/`DELETE` | `/notes/{id}` | Yes | Read, update or delete your note |

## Code

| File | Purpose |
| --- | --- |
| `backend/security.py` | Password hashing, creating and checking tokens |
| `backend/auth.py` | Register, login and `/auth/me` |
| `backend/notes.py` | Notes endpoints, all protected |
| `backend/models.py` | `users` table, and `user_id` on `notes` |

## Secret Key

The token signing key is stored in `backend/.env`, next to the database
password:

```bash
echo "SECRET_KEY=$(openssl rand -hex 32)" >> backend/.env
```

Anyone with this key could create valid tokens, so it is never committed to
Git.

## Database Change

The `notes` table already existed before authentication was added, so it
needed a new `user_id` column. This was done once with
`deploy/sql/add-note-owner.sql`:

```sql
DELETE FROM notes;
ALTER TABLE notes ADD COLUMN user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE;
CREATE INDEX ix_notes_user_id ON notes (user_id);
```

The old test notes were removed because they didn't belong to any user.

## Testing in the Browser

1. Open `http://127.0.0.1:8080/api/docs`
2. `POST /auth/register` with a username and password
3. Click **Authorize** at the top and log in with the same username and password
4. All `/notes` requests now send the token automatically

## Verification

Pending. To be recorded after the setup has been run on the server.
