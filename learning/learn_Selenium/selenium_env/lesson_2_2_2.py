from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(url)

def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))

def main_functions():

    get_x = browser.find_element(By.ID, 'input_value').text
    y = calc(get_x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script('return arguments[0].scrollIntoView();', button)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    button.click()

if __name__ == '__main__':
    try:
        main_functions()
    finally:
        time.sleep(7)
        browser.quit()
