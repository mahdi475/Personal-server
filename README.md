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
- [ ] Linux server environment
- [ ] SSH configuration
- [ ] Firewall configuration
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
