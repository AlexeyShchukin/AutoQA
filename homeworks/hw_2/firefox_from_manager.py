# pip install webdriver-manager

import pytest
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()


def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    about_link = driver.find_element(By.LINK_TEXT, "Новости")
    about_link.click()
    sleep(1)
    driver.save_screenshot("./ich_news.png")
    sleep(1)
