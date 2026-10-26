# PostgreSQL Database

PostgreSQL stores the API's data. FastAPI talks to it through SQLAlchemy.

```text
Client → Nginx → FastAPI → PostgreSQL
```

The client never talks to the database directly. Only the API knows the
database password, and the API decides what each request is allowed to do.

## Installation

```bash
sudo apt install postgresql -y
```

PostgreSQL runs as a systemd service and listens on `localhost:5432`. Port
5432 is not opened in UFW, so the database cannot be reached from outside the
server.

## Database and User

A dedicated database user is used instead of the `postgres` superuser. The
password is generated randomly and saved straight into `backend/.env`:

```bash
DB_PASSWORD=$(openssl rand -hex 16)
sudo -u postgres psql -c "CREATE USER personal_server WITH PASSWORD '$DB_PASSWORD';"
sudo -u postgres createdb -O personal_server personal_server
echo "DATABASE_URL=postgresql+psycopg://personal_server:$DB_PASSWORD@localhost:5432/personal_server" > backend/.env
chmod 600 backend/.env
```

| Name | Value |
| --- | --- |
| Database | `personal_server` |
| User | `personal_server` (owner of the database) |
| Password | Only stored in `backend/.env` |

## Configuration

`backend/.env` is listed in `.gitignore`, so the password is never pushed to
GitHub. `backend/.env.example` shows the format without the real password.

`backend/config.py` reads `DATABASE_URL` from the `.env` file.

## Code

| File | Purpose |
| --- | --- |
| `backend/config.py` | Reads settings from `.env` |
| `backend/database.py` | Connection to PostgreSQL and one session per request |
| `backend/models.py` | The `notes` table |
| `backend/schemas.py` | What the API accepts and returns |
| `backend/main.py` | The endpoints |

The `notes` table is created automatically when the API starts.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/health` | Checks that the API can reach the database |
| `GET` | `/notes` | List all notes |
| `POST` | `/notes` | Create a note |
| `GET` | `/notes/{id}` | Get one note |
| `PUT` | `/notes/{id}` | Update a note |
| `DELETE` | `/notes/{id}` | Delete a note |

All endpoints are also available through Nginx under `/api/`, for example
`/api/notes`, and can be tested in the browser at `/api/docs`.

## Useful Commands

```bash
sudo systemctl status postgresql                       # Is the database running?
sudo -u postgres psql -d personal_server               # Open the database
```

Inside `psql`:

```sql
\dt                     -- List tables
SELECT * FROM notes;    -- Show all notes
\q                      -- Quit
```

## Verification

Pending. To be recorded after the setup has been run on the server.
