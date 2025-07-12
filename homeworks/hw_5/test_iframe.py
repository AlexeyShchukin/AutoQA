import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()


def test_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    iframe = driver.find_element(By.ID, "my-iframe")
    driver.switch_to.frame(iframe)
    element = driver.find_element(By.ID, "content")
    assert "semper posuere integer et senectus justo curabitur." in element.text