from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calc(driver):

    delay = driver.find_element(By.ID, "delay")
    delay.click()
    delay.clear()
    delay.send_keys("3")
    element_7 = driver.find_element(By.CSS_SELECTOR, "div.keys>span:nth-child(1)")
    plus = driver.find_element(By.CSS_SELECTOR, "div.keys>span:nth-child(4)")
    el_8 = driver.find_element(By.CSS_SELECTOR, "div.keys>span:nth-child(2)")
    _equal = driver.find_element(By.CSS_SELECTOR, "div.keys>span:nth-child(15)")
    element_7.click()
    plus.click()
    el_8.click()
    _equal.click()

    wait = WebDriverWait(driver, 5)
    result_element = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
