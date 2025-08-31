import requests
import os
import pytest
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "status": {"type": "string"}
    },
    "required": ["status"]
}

def test_api_health():
    response = requests.get(
        'https://cires-wazuh-yahya.work.gd:55000/api/v3/healthcheck',
        auth=(os.getenv('API_USERNAME', 'wazuh-wui'), os.getenv('API_PASSWORD', 'k1b4n4#S3rv3r@2025#AP!')),
        verify=False
    )
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'
    validate(instance=response.json(), schema=schema)
