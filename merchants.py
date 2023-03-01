from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from constants import *


def save_merchant_screenshot():
    driver = webdriver.Firefox()
    driver.get(c.TARGET_URL)
    
    sleep(6)

    server_region = driver.find_element(By.ID, 'severRegion')
    select_server_region = Select(server_region)
    select_server_region.select_by_index(c.SERVER_REGION)

    server_region = driver.find_element(By.ID, 'server')
    select_server_region = Select(server_region)
    select_server_region.select_by_index(c.SERVER)

    sleep(1)

    driver.get_screenshot_as_file(SCREENSHOT)
    driver.quit()
