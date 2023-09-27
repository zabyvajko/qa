import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Petro")
    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Petrov")
    yourEmail = browser.find_element(By.XPATH, "/html/body/div/form/div/input[3]")
    yourEmail.send_keys("pp@gmail.com")

    chooseFile = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '123.txt')
    chooseFile.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    time.sleep(10)
    browser.quit()