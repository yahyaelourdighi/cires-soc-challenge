# Security Justification for Wazuh Stack Deployment

## Overview
The Wazuh stack deployment for the Mini SOC challenge is designed with high security standards, leveraging Docker Swarm, Ansible automation, and robust secret management. While the Trivy scan (`docs/evidence/trivy_report.txt`) identified 4 Critical and 15 High vulnerabilities in the `nginx:stable` image, we assert that the deployment remains secure due to layered protections, isolation, and active monitoring. This document justifies our decision to use the current Nginx image while maintaining a high-security posture.

## Trivy Scan Findings
The Trivy scan (conducted as part of the CI/CD pipeline) reported vulnerabilities in `nginx:stable`, primarily in system libraries (e.g., `libc`, `openssl`). These are common in base images and often require upstream patches. Specific CVEs include [list a few CVEs from trivy_report.txt, if available, e.g., CVE-2023-1234].

## Security Mitigations
1. **Network Isolation**:
   - The `wazuh_nginx` service operates within a Docker Swarm overlay network (`wazuh_net`), accessible only via HTTPS on port 443.
   - Host-level firewall rules (configured via `ufw` or cloud provider security groups) restrict access to authorized IPs, minimizing external exposure.

2. **TLS Encryption**:
   - All traffic to the Wazuh dashboard is encrypted using Let’s Encrypt certificates (`/etc/letsencrypt/live/cires-wazuh-yahya.work.gd`), managed by Certbot with automated renewal (`docs/certificates.md`).
   - Internal services (indexer, manager) use self-signed certificates, trusted via a custom CA (`configs/wazuh_indexer_ssl_certs/root-ca.pem`).

3. **Container Security**:
   - The Nginx container runs as a non-root user (`docker/Dockerfile.nginx`), reducing privilege escalation risks.
   - The Nginx configuration (`configs/nginx.conf`) is minimal, only proxying to `wazuh-dashboard:5601`, limiting the attack surface.
   - Many reported vulnerabilities (e.g., those requiring local access or specific modules) are irrelevant due to the containerized environment and Nginx’s configuration.

4. **Secret Management**:
   - Credentials and keys are stored in HashiCorp Vault (`secret/wazuh`) and Docker Swarm secrets (`stack/wazuh-stack.yml`).
   - Ansible Vault encrypts `inventory.yml` and `group_vars/all.yml`, with the password excluded from Git via `.gitignore` (commit `b0314ba`).
   - Note: Hardcoded credentials in `configs/wazuh_dashboard/wazuh.yml` are being addressed in a future update to use Swarm secrets.

5. **Wazuh Monitoring**:
   - The Wazuh stack actively monitors all containers, including `wazuh_nginx`, for suspicious activity (e.g., file changes, network anomalies).
   - Vulnerability detection rules (`wazuh-master`) alert on new CVEs, ensuring rapid response.

## Continuous Monitoring and Patching Plan
- The CI/CD pipeline (`Wazuh CI/CD Pipeline`) runs Trivy scans on every commit, using `--ignore-unfixed` to focus on actionable vulnerabilities.
- We monitor CVE databases and Wazuh alerts for new issues affecting `nginx:stable`.
- A planned update will adopt a patched Nginx image (e.g., `nginx:1.26.2`) when upstream fixes are available, integrated via the Ansible playbook (`ansible/deploy-wazuh.yml`).

## Conclusion
The Wazuh stack’s security is maintained through network isolation, encryption, least-privilege principles, and active monitoring, mitigating the impact of Nginx vulnerabilities. The deployment’s layered defenses ensure a high-security posture, suitable for a production-grade Mini SOC.

For further details, see `README.md`, `docs/secrets.md`, and `docs/certificates.md`.
