import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".trollface.btn").click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    findNumber = browser.find_element(By.ID, "input_value")
    x = findNumber.text
    y = calc(x)

    inputResult = browser.find_element(By.CLASS_NAME, "form-control")
    inputResult.send_keys(y)

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(10)
    browser.quit()

