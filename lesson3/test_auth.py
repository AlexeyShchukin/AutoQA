from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()


def login(driver, name: str = "", password: str = ""):
    driver.find_element(By.ID, "username").send_keys(name)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()


def test_happy_path(driver):
    login(driver, "tomsmith", "SuperSecretPassword!")
    success_message = "You logged into a secure area!"
    message_box = driver.find_element(By.ID, "flash")
    assert success_message in message_box.text
    assert "https://the-internet.herokuapp.com/secure" == driver.current_url


def test_incorrect_username(driver):
    login(driver, "Alex", "SuperSecretPassword!")
    error_message = "Your username is invalid!"
    message_box = driver.find_element(By.CSS_SELECTOR, ".flash.error")
    assert error_message in message_box.text


def test_incorrect_password(driver):
    login(driver, "tomsmith", "12325!")
    error_message = "Your password is invalid!"
    message_box = driver.find_element(By.CSS_SELECTOR, ".flash.error")
    assert error_message in message_box.text
