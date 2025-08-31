## Self-Hosted Runner Prerequisites

To run the CI/CD pipeline, self-hosted runners must have the following installed:
- **Docker**: Latest stable version (e.g., 20.10 or higher) with `docker.io` package.
- **Ansible**: Version 2.9 or higher (`ansible-core`).
- **Python**: Version 3.8 or higher with `pip3`.
- **Trivy**: Latest version for container image scanning.
- **Chrome/Chromedriver**: Chrome browser and compatible Chromedriver for Selenium tests.
- **Linting Tools**: `ansible-lint` and `yamllint` for code quality checks.
- **Additional Packages**: `certbot`, `python3-certbot-nginx`, `python3-docker`.

**Setup Commands** (Ubuntu-based runner):
```bash
sudo apt update
sudo apt install -y docker.io python3-pip python3-docker certbot python3-certbot-nginx
pip3 install ansible ansible-lint yamllint
curl -fsSL https://github.com/aquasecurity/trivy/releases/latest/download/trivy_*.deb -o trivy.deb
sudo dpkg -i trivy.deb
sudo apt install -y chromium-browser chromium-chromedriver
