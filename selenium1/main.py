from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


#keeping web browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/cookieclicker/')

try:
    consent = driver.find_element(By.CSS_SELECTOR, "button[class='fc-button fc-cta-consent fc-primary-button']")
    consent.click()
    lang = driver.find_element(By.CSS_SELECTOR, "div[id='langSelect-EN']")
    lang.click()

except:
    pass

finally:
    pass

game = True

current_product_id = 0
current_product_quantity = 0
current_upgrade = 0

while game:
    cookie = driver.find_element(By.CSS_SELECTOR, "button[id='bigCookie']")
    cookie.click()

    try:
        if current_product_quantity < 5:
            try:
                click_upgrade = driver.find_element(By.CSS_SELECTOR, f"div[class='product unlocked enabled'][id='product{current_product_id}']")
                click_upgrade.click()
                current_product_quantity += 1
            except NoSuchElementException:
                pass
            finally:
                pass
        else:
            try:
                upgrade = driver.find_element(By.CSS_SELECTOR, f"div[id='upgrade{current_upgrade}']")
                upgrade.click()
                #current_upgrade += 1
                current_product_id += 1
                current_product_quantity = 0
            finally:
                pass

    finally:
        pass

#driver.quit()
