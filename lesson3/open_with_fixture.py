from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_about_page(driver):
    # Открытие сайта
    driver.get("https://itcareerhub.de/ru")

    # Явное ожидание, чтобы ссылка "О нас" появилась на странице
    sleep(2)
    about_link = driver.find_element(By.LINK_TEXT, "О нас")
    about_link.click()
    sleep(2)
