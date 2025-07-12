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


def test_upload(driver):
    url = "https://the-internet.herokuapp.com/upload"
    driver.get(url)

    # Находим input-элемент
    file_input = driver.find_element(By.ID, "file-upload")

    # Указываем путь к файлу
    file_path = "C:\Images\My_city.jpg"
    file_input.send_keys(file_path)

    # Отправляем форму (если требуется)
    submit_button = driver.find_element(By.ID, "file-submit")
    submit_button.click()

    wait = WebDriverWait(driver, 10)
    file_name = "My_city.jpg"
    assert wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > div > h3"), "File Uploaded!"))
    assert wait.until(EC.text_to_be_present_in_element((By.ID, "uploaded-files"), file_name))
