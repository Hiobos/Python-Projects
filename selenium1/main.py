from selenium import webdriver
from selenium.webdriver.common.by import By

#keeping web browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://store.steampowered.com/')

element_menu = driver.find_element(By.CLASS_NAME, 'header_installsteam_btn_content')
element_menu.click()