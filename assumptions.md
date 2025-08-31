## Assumptions

This project makes the following assumptions:

### DNS and Domain
- A domain (`cires-wazuh-yahya.work.gd`) is configured to point to the public IP (`52.0.98.231`) of the Docker Swarm manager.
- DNS resolution is managed externally and is accessible during deployment.

### TLS Certificates
- Let's Encrypt is available for certificate provisioning and renewal for the domain `cires-wazuh-yahya.work.gd`.
- The runner has internet access to communicate with Let's Encrypt servers.
- Self-signed certificates are used for internal Wazuh component communications, with a root CA trusted by all containers.

### Runner Permissions
- The self-hosted GitHub Actions runner has:
  - Sudo privileges to install packages (`docker.io`, `certbot`, etc.).
  - SSH access to the Swarm manager (`52.0.98.231`) with key `~/.ssh/id_ed25519`.
  - Write permissions to `/etc/wazuh`, `/etc/nginx`, and `/etc/letsencrypt` directories.
- The runner has a valid Vault token for accessing secrets at `http://127.0.0.1:8200`.

### IP and Networking
- The Swarm manager is accessible at the public IP `52.0.98.231`.
- The overlay network `wazuh_net` is created and attachable for service communication.
- Ports 80, 443, 514 (UDP), 1514, 1515, 55000, 5601, and 9200 are open on the Swarm manager's firewall.

### Vault and Secrets
- HashiCorp Vault is running locally (`http://127.0.0.1:8200`) on the Swarm manager or runner.
- Secrets are pre-populated in Vault at `secret/wazuh` with required credentials.
