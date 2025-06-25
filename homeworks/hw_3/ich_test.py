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
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_logo_exists(driver):
    element = driver.find_element(
        By.CSS_SELECTOR,
        "img.tn-atom__img"
    )
    assert element.is_displayed()


def test_links_exist(driver):
    links = [
        "Программы",
        "Способы оплаты",
        "Новости",
        "О нас",
        "Отзывы"
    ]

    for link in links:
        element = driver.find_element(By.LINK_TEXT, link)
        assert element.is_displayed()


def test_lang_switcher(driver):
    lang_link = driver.find_element(By.LINK_TEXT, "de")
    sleep(2)
    lang_link.click()
    sleep(2)
    current_url = driver.current_url
    sleep(2)
    assert current_url == "https://itcareerhub.de/"


def test_phone_icon(driver):
    element = driver.find_element(
        By.CSS_SELECTOR,
        "#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221710153310161 > a"
    )
    element.click()
    res = driver.find_element(
        By.CSS_SELECTOR,
        '#rec767956167 > div > div > div.t396__elem.tn-elem.tn-elem__7679561671711363912027 > div'
    )
    assert res.text == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
    assert res.is_displayed()
