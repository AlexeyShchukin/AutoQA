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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


def test_images(driver):
    wait = WebDriverWait(driver, 15)
    el = wait.until(EC.visibility_of_element_located((By.ID, "award")))
    assert el.get_attribute("alt") == "award"
