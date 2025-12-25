from selenium import webdriver
from selenium.webdriver.common.by import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.python.org/")


holder = {}
time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
for index in range(len(names)):
    holder[index] = {
        "time": time[index].text,
        "name": names[index].text
    }

print(holder)


driver.quit()
