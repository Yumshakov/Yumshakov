from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, 'first_name')
    input_name.send_keys('Ivan')
    input_last_name = browser.find_element(By.NAME, 'last_name')
    input_last_name.send_keys('Petrov')
    input_city = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input_city.send_keys('Moskow')
    input_country = browser.find_element(By.ID, 'country')
    input_country.send_keys('Russia')
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
