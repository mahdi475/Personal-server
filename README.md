# Personal Server

A self-hosted Linux backend platform built to learn server administration,
networking, backend development, security, deployment and DevOps.

## Project Goals

- Linux server administration
- SSH and networking
- REST API
- PostgreSQL
- Authentication
- Docker
- Nginx
- HTTPS
- Redis
- Logging
- Monitoring
- Automated testing
- CI/CD
- Cloud deployment

## Roadmap

- [x] Project setup
- [x] Git & GitHub
- [x] Linux server environment
- [x] SSH configuration
- [x] Firewall configuration
- [ ] FastAPI backend
- [ ] PostgreSQL database
- [ ] Authentication
- [ ] Docker
- [ ] Redis
- [ ] Nginx reverse proxy
- [ ] HTTPS
- [ ] Logging
- [ ] Monitoring
- [ ] Automated tests
- [ ] CI/CD
- [ ] Cloud deployment

## Current Server Environment

The initial Ubuntu VM setup is documented in
[docs/server-setup.md](docs/server-setup.md).

Verified so far:

- Ubuntu Server 26.04 LTS running in Oracle VM VirtualBox
- VM name: `Personal-Server`
- Hostname: `personalserver`
- Linux user: `mahdi`
- VirtualBox NAT networking through `enp0s3`
- DHCP IPv4 address: `10.0.2.15/24`
- CPU cores: `2`
- Memory: `3.3 GiB`
- Virtual disk: `Personal-Server.vdi`, 25 GB
- Root filesystem: 12G total, 5.3G used, 5.5G available
- OpenSSH Server active and listening on port 22
- UFW firewall active with SSH allowed on port 22
- Internet access tested with `ping`
- HTTPS access tested with `curl`

## Architecture

```text
Client
   |
   v
Nginx
   |
   v
FastAPI
   |
   +---- PostgreSQL
   |
   +---- Redis
```
