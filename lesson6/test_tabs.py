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
    

def test_with_tabs(driver):
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    button = driver.find_element(By.CLASS_NAME, "trollface")
    button.click()
    tab = driver.window_handles[1]
    driver.switch_to.window(tab)
    sleep(2)
    text = driver.find_element(By.CSS_SELECTOR, "#simple_text").text
    assert text == "Math is real magic!"