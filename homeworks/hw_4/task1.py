import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_check_button(driver):
    element = driver.find_element(By.CSS_SELECTOR,  "input[fdprocessedid='zkp0bq']")
    element.click()
    element.send_keys("ITCH")
    button = driver.find_element(By.CLASS_NAME, "btn btn-primary")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR,  "input[fdprocessedid='zkp0bq']"), "ITCH")





