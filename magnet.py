# %%
from bs4 import BeautifulSoup
import requests
import re

# %%
req = requests.get("https://nyaa.si")
html = req.text
soup = BeautifulSoup(html, "html.parser")

# %%
my_titles = soup.select("body > div > div.table-responsive > table > tbody > tr td > a")
my_titles

# %%
for i in my_titles:
    print(i['href'])
# %%
