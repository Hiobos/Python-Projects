from selenium import webdriver
from selenium.webdriver.common.by import By

#keeping web browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')

event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')

for time in event_times:
    print(time.text)

for name in event_names:
    if name.text != 'More':
        print(name.text)


driver.quit()
