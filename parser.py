import requests
from bs4 import BeautifulSoup

req = requests.get("https://nyaa.si")
html = req.text
soup = BeautifulSoup(html, "html.parser")

# NOTE - Get title from Site
# body > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
my_titles = soup.select(
    "body > div > div.table-responsive > table > tbody > tr > td > a"
)
for i in my_titles:
    i.text.replace(" ", "_")
    print(i.text)

# body > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
# body > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(3) > a:nth-child(2)