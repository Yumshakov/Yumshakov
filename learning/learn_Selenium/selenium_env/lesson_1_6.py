from selenium import webdriver
import math
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    link_find = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    link_find.click()
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

