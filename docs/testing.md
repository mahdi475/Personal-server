# Automated Tests

The API is tested with `pytest`. The tests send real HTTP requests to the app
and check the answers, so mistakes are caught before they reach the server.

## Running the Tests

```bash
cd ~/personal-server/backend
venv/bin/pip install -r requirements-dev.txt
venv/bin/pytest -v
```

## Test Database

The tests never touch the real PostgreSQL database. `tests/conftest.py`
points the app to a temporary SQLite file instead, and every test starts with
empty tables.

## What Is Tested

| File | Checks |
| --- | --- |
| `tests/test_health.py` | `/` and `/health` answer correctly |
| `tests/test_auth.py` | Register, duplicate usernames, short passwords, wrong password, fake tokens |
| `tests/test_notes.py` | Login is required, create/list/update/delete, users can't see each other's notes |

## Verification

Pending. To be recorded after the tests have been run on the server.
