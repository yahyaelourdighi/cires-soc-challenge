import requests
import os
import pytest

def test_api_health():
    response = requests.get(
        'https://cires-wazuh-yahya.work.gd/api/v3/healthcheck',
        auth=(os.getenv('API_USERNAME', 'wazuh-wui'), os.getenv('API_PASSWORD', 'MyS3cr37P450r.*-'))
    )
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'
