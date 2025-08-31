## Certificate Management
- **Let’s Encrypt**:
  - Certificates for `cires-wazuh-yahya.work.gd` are obtained via Certbot (`certbot certonly --standalone`).
  - Stored in `/etc/letsencrypt/live/cires-wazuh-yahya.work.gd`.
  - Auto-renewed via cron job: `certbot renew --quiet --deploy-hook 'docker service update --force wazuh_nginx'` (runs at 00:00 and 12:00 daily).
- **Internal CA**:
  - Self-signed certificates for Wazuh components (indexer, manager, dashboard) are generated using `openssl`.
  - Root CA: `/etc/wazuh/certs/root-ca.pem`.
  - Trust setup: Certificates are mounted to containers and referenced in configurations (e.g., `opensearch_dashboards.yml`, `filebeat.yml`).
  - To trust the CA on a client:
    ```bash
    sudo cp root-ca.pem /usr/local/share/ca-certificates/wazuh-root-ca.crt
    sudo update-ca-certificates
