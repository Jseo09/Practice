import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AMAZON_LINK = "https://www.amazon.com/Beats-Solo-Ear-Headphones-Compatible/dp/B0CZPGX972"

opts = Options()
opts.add_argument("--start-maximized")
opts.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=opts)
driver.get(AMAZON_LINK)

wait = WebDriverWait(driver, 20)


title_el = wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
title = title_el.text.strip()

price = None
selectors = [
    "#corePrice_feature_div span.a-offscreen",
    "span.a-price span.a-offscreen",
    "#priceblock_dealprice",
    "#priceblock_ourprice",
]
for css in selectors:
    els = driver.find_elements(By.CSS_SELECTOR, css)
    if els and els[0].text.strip():
        price = els[0].text.strip()
        break

driver.quit()

print("TITLE:", title)
print("PRICE:", price)

if price:
    m = re.search(r"(\d+(?:\.\d+)?)", price.replace(",", ""))
    if m:
        price_value = float(m.group(1))
        print("PRICE_VALUE:", price_value)

soup = BeautifulSoup(response, "html.parser")
print(soup)
# price = soup.find(id="twister-plus-price-data-price")
# print(price)
title = soup.find(class_='a-size-large product-title-word-break')
print(title.text.strip())

if float(price) < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("xxxxxx@gmail.com", "xxxxxxxxx")
        connection.sendmail(
            from_addr="xxxx@gmail.com",
            to_addrs="xxxx@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )

