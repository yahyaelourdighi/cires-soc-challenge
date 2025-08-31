## Troubleshooting

### Nginx Service Failures
- **Check Logs**: `docker service logs wazuh_nginx`
- **Validate Connectivity**: `docker exec -it <nginx_container_id> curl -s -k -u kibanaro:<password> https://wazuh-dashboard:5601`
- **Verify Secrets**: `docker secret ls`
- **Test Nginx Config**: `docker run --rm -v $(pwd)/configs/nginx.conf:/etc/nginx/nginx.conf:ro nginx:stable nginx -t`
- **Check Certificates**: `docker exec -it <nginx_container_id> ls -l /etc/letsencrypt/live/cires-wazuh-yahya.work.gd`
