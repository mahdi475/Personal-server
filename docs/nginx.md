# Nginx Web Server

Nginx was installed on the Ubuntu Server and configured to serve a custom
website.

## Installation

```bash
sudo apt update
sudo apt install nginx -y
```

## Custom Site

The website files are stored in:

```text
/var/www/personal-server
```

The Nginx site configuration is:

```text
/etc/nginx/sites-available/personal-server
```

The configuration is enabled through:

```text
/etc/nginx/sites-enabled/personal-server
```

## Configuration

The configuration used by the server is stored in:

```text
nginx/personal-server.conf
```

## Verification

Nginx configuration was tested with:

```bash
sudo nginx -t
```

Result:

```text
syntax is ok
test is successful
```

Nginx was verified as running with:

```bash
sudo systemctl status nginx
```

The service was active and running.

The website was tested locally with:

```bash
curl http://localhost
```

The server returned the custom HTML page.

## Firewall

HTTP traffic was allowed through UFW:

```bash
sudo ufw allow 80/tcp
```

## Local Access

VirtualBox NAT port forwarding was configured to forward:

```text
Host port: 8080
Guest port: 80
```

The website was then accessible from the Windows host at:

```text
http://127.0.0.1:8080
```

This confirms that the Ubuntu server is serving the custom website through
Nginx.
