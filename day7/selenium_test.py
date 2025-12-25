from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.amazon.com/dp/B0FZBN6LYF")
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
price_el = driver.find_element(By.ID, "attach-base-product-price")
price = price_el.get_attribute("value")
print(f"The price is {price}")
print("has attach id?", "attach-base-product-price" in driver.page_source)
print(driver.title)
driver.quit()
