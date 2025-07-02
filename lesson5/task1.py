import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.devtools.v135.debugger import pause

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_header_text(driver):
    driver.implicitly_wait(10)
    element = driver.find_element(By.CSS_SELECTOR, "img[imgfield='tn_img_1710153310161']")
    element.click()
    sleep(1)
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.presence_of_element_located((By.ID, "some_id")))