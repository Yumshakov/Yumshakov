from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, '[type=text]')
    for element in elements:
        element.send_keys('My response')

    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

except:
    time.sleep(30)
    browser.quit()
