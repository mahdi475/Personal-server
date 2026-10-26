# Systemd Service

The FastAPI backend runs as a systemd service. This means:

- the API starts automatically when the server boots
- the API is restarted automatically if it crashes
- the API keeps running after the SSH session is closed

Before this, Uvicorn had to be started by hand in a terminal.

## Service File

The service file is stored in the repository:

```text
deploy/personal-server-api.service
```

It is installed on the server as:

```text
/etc/systemd/system/personal-server-api.service
```

Main settings:

| Setting | Purpose |
| --- | --- |
| `User=mahdi` | The API runs as a normal user, not as root |
| `WorkingDirectory` | The folder that contains `main.py` |
| `ExecStart` | Starts Uvicorn from the virtual environment |
| `--host 127.0.0.1` | The API only listens inside the server, so outside traffic must go through Nginx |
| `--root-path /api` | Tells FastAPI that Nginx serves it under `/api`, so the API docs work at `/api/docs` |
| `Restart=always` | systemd starts the API again if it stops |
| `After=postgresql.service` | At boot, the API starts after the database |
| `WantedBy=multi-user.target` | The service starts at boot |

## Installation

```bash
cd ~/personal-server
python3 -m venv backend/venv
backend/venv/bin/pip install -r backend/requirements.txt

sudo cp deploy/personal-server-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now personal-server-api
```

`daemon-reload` makes systemd read the new file. `enable --now` starts the
service now and also at every boot.

## Useful Commands

```bash
systemctl status personal-server-api        # Is it running?
sudo systemctl restart personal-server-api  # Restart after code changes
journalctl -u personal-server-api -f        # Follow the API logs
```

## Verification

After installation, the service was checked with:

```bash
systemctl status personal-server-api --no-pager
```

Result:

```text
Loaded: loaded (/etc/systemd/system/personal-server-api.service; enabled; preset: enabled)
Active: active (running)
```

The API was then opened from the Windows host through Nginx at:

```text
http://127.0.0.1:8080/api/docs
```

The Swagger UI loaded, and `GET /` returned `200` with the JSON message. The
response header `server: nginx/1.28.3 (Ubuntu)` confirms that the request went
through Nginx.

Still pending: confirming that the service starts by itself after a reboot.
