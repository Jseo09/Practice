from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value = 'fName')
first_name.send_keys("dadasdastest")
last_name = driver.find_element(By.NAME, value = 'lName')
last_name.send_keys("dasdasd")
email_address = driver.find_element(By.NAME, value = 'email')
email_address.send_keys("dasdsdd@gmail.com")

click_button = driver.find_element(
    By.CSS_SELECTOR,
    ".btn.btn-lg.btn-primary.btn-block"
)
click_button.click()
