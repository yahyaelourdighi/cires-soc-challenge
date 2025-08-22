import requests
import json
import os
import ssl
import certifi

def test_wazuh_api():
    url = f"{os.environ['WAZUH_API_URL']}/health"
    headers = {
        "Authorization": f"Basic {os.environ['API_USERNAME']}:{os.environ['API_PASSWORD']}"
    }
    context = ssl.create_default_context(cafile=certifi.where())
    
    try:
        response = requests.get(url, headers=headers, verify=context)
        assert response.status_code == 200, f"API health check failed: {response.status_code}"
        data = response.json()
        assert data.get('status') == 'ok', f"API status is not ok: {data.get('status')}"
        print("API health check passed successfully")
    except Exception as e:
        print(f"API health check failed: {str(e)}")
        raise

if __name__ == "__main__":
    test_wazuh_api()
