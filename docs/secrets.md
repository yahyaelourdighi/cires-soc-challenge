## Secret Rotation
- **Wazuh Credentials**:
  - Update `secret/wazuh` in HashiCorp Vault using `vault kv put secret/wazuh ...`.
  - Restart services: `docker service update --force wazuh_wazuh-master wazuh_wazuh-dashboard`.
- **TLS Certificates**:
  - Let’s Encrypt certificates auto-renew via Certbot cron job.
  - For internal CA certificates, regenerate using `openssl` and update Swarm secrets:
    ```bash
    openssl genrsa -out new-key.pem 2048
    openssl req -new -key new-key.pem -out new.csr
    vault kv put secret/wazuh/tls new-key=@new-key.pem
    docker secret rm wazuh_api_password && docker secret create wazuh_api_password new-key.pem
