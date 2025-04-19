from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

#keeping web browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = uc.Chrome(options=chrome_options)
driver.get('https://csgo-skins.com/')
