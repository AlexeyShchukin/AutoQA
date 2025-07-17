import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_success_login_valid_data(driver):
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("standard_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Не удалось войти в систему."
    inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")
    assert inventory_list, "Список товаров не найден на странице."


def test_invalid_password(driver):
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("standard_user")

    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("wrong_password")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Username and password do not match" in error_message.text, "Неверное сообщение об ошибке."


def test_locked_out_user(driver):
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("locked_out_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Sorry, this user has been locked out." in error_message.text, "Неверное сообщение об ошибке."


def test_empty_username(driver):
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Username is required" in error_message.text, "Неверное сообщение об ошибке."


def test_empty_password(driver):
    user_name_input_field = driver.find_element(By.ID, "user-name")
    user_name_input_field.send_keys("standard_user")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message, "Сообщение об ошибке не отображается."
    assert "Password is required" in error_message.text, "Неверное сообщение об ошибке."
