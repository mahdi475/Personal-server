# FastAPI Backend

## Overview

The Personal Server backend is built with FastAPI and runs on the Ubuntu Server.

FastAPI provides the API layer while Uvicorn is used as the ASGI server.

## Environment

- Ubuntu Server 26.04 LTS
- Python 3.14
- FastAPI
- Uvicorn
- Python virtual environment

## Project structure

```text
Personal-server/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── deploy/
│   └── personal-server-api.service
├── nginx/
│   └── personal-server.conf
└── docs/
    └── fastapi.md
```

## FastAPI application

The API is defined in:

```text
backend/main.py
```

The application currently contains a root endpoint:

```text
GET /
```

The endpoint returns:

```json
{
    "message": "Mahdi's Personal Server API is running!"
}
```

## Running FastAPI

A Python virtual environment in `backend/venv` is used to isolate the backend
dependencies.

On the server, the API is run by systemd. See [systemd.md](systemd.md).

For a manual test, stop the service first and start Uvicorn by hand:

```bash
sudo systemctl stop personal-server-api
cd backend
source venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000 --root-path /api
```

Uvicorn listens on `127.0.0.1:8000`, so the API can only be reached from inside
the server. Traffic from outside has to go through Nginx.

`--root-path /api` tells FastAPI that Nginx serves it under `/api`, so the
interactive API docs work at `/api/docs`.

## Nginx reverse proxy

Nginx is used as a reverse proxy in front of FastAPI.

Requests sent to:

```text
/api/
```

are forwarded by Nginx to:

```text
http://127.0.0.1:8000/
```

This separates the public HTTP server from the backend application.

The flow is:

```text
Client
  ↓
Nginx :80
  ↓
/api/
  ↓
FastAPI :8000
  ↓
JSON response
```

## Verification

The FastAPI application was tested directly:

```bash
curl http://localhost:8000
```

The response was:

```json
{
    "message": "Mahdi's Personal Server API is running!"
}
```

The Nginx reverse proxy was then tested with:

```bash
curl http://localhost/api/
```

The same JSON response was returned.

This confirms that Nginx successfully forwards API requests to the FastAPI
backend.

## Current status

- FastAPI installed and configured
- Uvicorn configured as the application server
- API endpoint implemented
- Nginx reverse proxy configured
- API tested successfully through Nginx
