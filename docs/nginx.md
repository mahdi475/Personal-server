# Nginx Web Server

Nginx was installed on the Ubuntu Server and configured to serve a custom
HTML page.

## Installation

```bash
sudo apt update
sudo apt install nginx -y
```

## Verification

Nginx was verified with:

```bash
sudo systemctl status nginx
```

Result:

```text
Active: active (running)
```

The server was also tested locally with:

```bash
curl http://localhost
```

The response returned the custom HTML page.

## Firewall

HTTP traffic was allowed through UFW:

```bash
sudo ufw allow 80/tcp
```

## Local Deployment

VirtualBox NAT port forwarding was configured:

```text
Host: 8080
Guest: 80
```

The custom page was then accessible from the Windows host at:

```text
http://127.0.0.1:8080
```

This confirms that the Ubuntu server is successfully serving a custom website
through Nginx.
