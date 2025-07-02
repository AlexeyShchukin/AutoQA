import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    yield driver
    driver.quit()


def test_checkbox(driver):
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
    sleep(1)
    checkbox.click()
    sleep(1)
    assert checkbox.get_attribute("checked") == "true"


def test_checkbox2(driver):
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
    sleep(1)
    checkbox.click()
    sleep(1)
    assert not checkbox.is_selected()
