# Server Setup

This document records the initial Ubuntu Server setup for the Personal Server
project.

Only facts observed during the setup session are listed as verified. Anything
that still needs more testing is marked as pending instead of guessed.

## Verified Environment

| Area | Value |
| --- | --- |
| Host machine | Windows 11 |
| Virtualization | Oracle VM VirtualBox |
| VM name | Personal-Server |
| Guest OS | Ubuntu Server 26.04 LTS |
| Installer ISO | ubuntu-26.04-live-server-amd64.iso |
| Hostname | personalserver |
| Linux user | mahdi |
| Network mode | VirtualBox NAT |
| Network interface | enp0s3 |
| IPv4 address | 10.0.2.15/24 via DHCPv4 |
| CPU cores | 2 |
| Memory | 3.3 GiB total |
| Swap | 2.0 GiB total, 0 B used |
| Virtual disk | Personal-Server.vdi, 25 GB |
| Root filesystem | 12G total, 5.3G used, 5.5G available, 50% used |
| Boot filesystem | 2.0G total, 187M used, 1.7G available, 11% used |
| SSH | OpenSSH Server installed and running |
| Firewall | UFW active, allowing SSH on port 22 |
| Ubuntu Pro | Skipped during installation |
| Featured server snaps | None selected |

## Verified Checks

| Check | Command or installer step | Result |
| --- | --- | --- |
| Login | Ubuntu login prompt | User `mahdi` could log in |
| Hostname | `hostname` | `personalserver` |
| Current user | `whoami` | `mahdi` |
| Network interface | `ip addr` | `enp0s3` had IPv4 address `10.0.2.15/24` |
| Root disk usage | `df -h` | `/` had 12G total, 5.3G used, 5.5G available |
| Boot disk usage | `df -h` | `/boot` had 2.0G total, 187M used, 1.7G available |
| Memory | `free -h` | 3.3 GiB total, 462 MiB used, 2.9 GiB available |
| Swap | `free -h` | 2.0 GiB total, 0 B used |
| CPU cores | `nproc` | 2 |
| Package network access | `sudo apt update` | Package index update succeeded |
| Internet connectivity | `ping -c 4 google.com` | Server received replies |
| HTTPS connectivity | `curl -I https://ubuntu.com` | Server received an HTTP response |
| SSH installation | Ubuntu installer SSH step | OpenSSH Server was installed |
| SSH service | `sudo systemctl status ssh` | `ssh.service` was active and running |
| SSH port | `sudo systemctl status ssh` | SSH was listening on `0.0.0.0:22` and `[::]:22` |
| Firewall status | `sudo ufw status` | UFW was active |
| Firewall rule | `sudo ufw status` | `22/tcp` was allowed from anywhere for IPv4 and IPv6 |

## Notes

- The VirtualBox VM is named `Personal-Server`, but the Ubuntu hostname is
  `personalserver`.
- The SSH status output showed `ssh.service` as active and running. It also
  showed the service unit as `disabled` and triggered by `ssh.socket`, so boot
  behavior can be re-checked later if needed.
- The VM disk is configured as 25 GB, while the root filesystem currently uses a
  12G logical volume.

## Not Configured Yet

- SSH key-based authentication
- Remote SSH login from Windows
- FastAPI backend
- PostgreSQL
- Docker
- Nginx
- HTTPS
- Monitoring
- CI/CD

## Next Manual Steps

Before marking remote access as complete, test SSH from Windows. With VirtualBox
NAT, this may require port forwarding or a different network mode before Windows
can connect to the Ubuntu guest.

The next server-side checks are:

```bash
sudo systemctl status ssh
sudo ufw status
```
