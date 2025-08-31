from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_dashboard_access(browser):
    browser.get('https://cires-wazuh-yahya.work.gd')
    assert browser.title == 'Wazuh'
    login_form = browser.find_element(By.ID, 'login-form')
    assert login_form.is_displayed()

def test_login(browser):
    browser.get('https://cires-wazuh-yahya.work.gd')
    username = browser.find_element(By.ID, 'username')
    password = browser.find_element(By.ID, 'password')
    login_button = browser.find_element(By.ID, 'login-button')
    username.send_keys(os.getenv('READALL_USERNAME', 'github_user'))
    password.send_keys(os.getenv('READALL_PASSWORD'))
    login_button.click()
    dashboard_element = browser.find_element(By.CLASS_NAME, 'dashboard-home')
    assert dashboard_element.is_displayed()
