# pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


service = Service("C://Program Files/ChromDriver/chromedriver.exe")
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1024, 768)

driver.get("https://itcareerhub.de/ru")
sleep(2)
about_link = driver.find_element(By.LINK_TEXT, "О нас")
about_link.click()
sleep(2)
driver.refresh()
sleep(2)
driver.get("https://www.berlin.de")
driver.save_screenshot("./berlin_screenshot.png")
sleep(2)
driver.back()

sleep(2)
