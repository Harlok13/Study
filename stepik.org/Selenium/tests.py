import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)
driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, '.textarea')

textarea.send_keys('get()')
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, '.submit-submission')

submit_button.click()
time.sleep(5)

driver.quit()
