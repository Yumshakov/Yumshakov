from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(url)

def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))

def main_functions():

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(y)
    checkbox_select = browser.find_element(By.ID, "robotCheckbox")
    checkbox_select.click()
    radiobut_select = browser.find_element(By.ID, "robotsRule")
    radiobut_select.click()
    btn_submit = browser.find_element(By.CSS_SELECTOR, "button")
    btn_submit.click()

if __name__ == '__main__':
    try:
        main_functions()
    finally:
        time.sleep(3)
        browser.quit()
