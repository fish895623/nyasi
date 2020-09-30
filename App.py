import sys

import bs4
import requests
from selenium import webdriver

# Driver option
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
)

driver = webdriver.Chrome('chromedriver', options=options)
driver.get(
    'https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html'
)


def main():
    User_agent = driver.find_element_by_xpath(
        "/html/body/div/div[1]/nav/ul/li[1]/ul/li[1]/a")
    print(User_agent.text)
    # /html/body/div/div[1]/nav/ul/li[1]/ul/li[1]
    # /html/body/div/div[1]/nav/ul/li[1]/ul/li[1]/a/text()
    # /html/body/div/div[1]/nav/ul/li[1]/ul/li[2]


if __name__ == "__main__":
    main()
# /html/body/div[2]/div[3]/div[1]/div/h3