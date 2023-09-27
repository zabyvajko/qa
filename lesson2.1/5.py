import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    result = browser.find_element(By.CSS_SELECTOR, ".form-control")
    result.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobutton.click()

    submitbutton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitbutton.click()



finally:
    time.sleep(10)
    browser.quit()



