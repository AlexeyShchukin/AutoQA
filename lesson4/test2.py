import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    driver.get("https://suninjuly.github.io/cats.html")
    yield driver
    driver.quit()


def test_element_exists(driver):
    element = driver.find_element(By.CSS_SELECTOR, "body > main > div > div > div > div:nth-child(4) > div")
    assert element.is_displayed()


def test_count_images(driver):
    elements = driver.find_elements(By.TAG_NAME, "img")
    assert len(elements) == 6