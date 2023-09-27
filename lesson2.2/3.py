import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)
try:
    
    numOne = browser.find_element(By.ID, "num1")
    num1 = numOne.text
    numTwo = browser.find_element(By.ID, "num2")
    num2 = numTwo.text
    sum = int(num1) + int(num2)
    sum1 = str(sum)
    print(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum1)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)

    browser.quit()