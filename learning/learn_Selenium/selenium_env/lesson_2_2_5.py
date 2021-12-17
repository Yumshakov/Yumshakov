from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))

def main_functions():

    browser.get(url)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    find_attribute = browser.find_element(By.ID, 'input_value')
    y = calc(find_attribute.text)
    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(y)
    btn_submit = browser.find_element(By.CSS_SELECTOR, "button")
    btn_submit.click()

if __name__ == '__main__':
    try:
        url = "http://suninjuly.github.io/redirect_accept.html"
        browser = webdriver.Chrome()
        main_functions()
    finally:
        time.sleep(7)
        browser.quit()
