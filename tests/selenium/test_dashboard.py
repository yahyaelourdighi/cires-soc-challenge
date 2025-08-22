from selenium import webdriver
from selenium.webdriver.chrome.options import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_wazuh_dashboard():
    # Set up Chrome options for headless mode
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to Wazuh dashboard
        driver.get(os.environ['WAZUH_URL'])

        # Verify HTTPS
        assert driver.current_url.startswith('https://'), "Dashboard is not served over HTTPS"

        # Wait for page to load
        WebDriverWait(driver, 10).until(EC.title_contains("Wazuh"))

        # Verify page title
        assert "Wazuh" in driver.title, "Page title does not contain 'Wazuh'"

        # Verify login form elements
        username_field = driver.find_element(By.ID, 'username')
        password_field = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.CLASS_NAME, 'btn-login')
        assert username_field, "Username field not found"
        assert password_field, "Password field not found"
        assert login_button, "Login button not found"

        # Optional: Test login with non-admin account
        username_field.send_keys(os.environ['TEST_USERNAME'])
        password_field.send_keys(os.environ['TEST_PASSWORD'])
        login_button.click()

        # Wait for dashboard to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'sidebar'))
        )
        assert driver.find_element(By.CLASS_NAME, 'sidebar'), "Dashboard sidebar not found"

        print("All dashboard tests passed successfully")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_wazuh_dashboard()
