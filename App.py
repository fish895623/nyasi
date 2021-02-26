import sys

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# Driver option
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-gpu")
options.add_argument(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
)

driver = webdriver.Chrome("chromedriver", options=options)
driver.get("https://beomi.github.io/beomi.github.io_old/")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# notices = soup.select("body > h3:nth-child(4) > a")
notice = soup.select("body h3 > a")
for i in notice:
    print(i.text)
