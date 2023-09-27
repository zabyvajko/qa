import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    findNumber = browser.find_element(By.ID, "input_value")
    x = findNumber.text
    y = calc(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    inputResult = browser.find_element(By.ID, "answer")
    inputResult.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submitbutton = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitbutton.click()

finally:
    time.sleep(10)
    browser.quit()