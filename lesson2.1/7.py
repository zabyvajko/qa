import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    value = x_element.get_attribute("valuex")
    x = value
    y = calc(x)

    result = browser.find_element(By.ID, "answer")
    result.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submitbutton = browser.find_element(By.CSS_SELECTOR, ".btn")
    submitbutton.click()



finally:
    time.sleep(10)
    browser.quit()



