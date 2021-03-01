# %%
import re

import requests
from bs4 import BeautifulSoup

req = requests.get("https://nyaa.si")
html = req.text
soup = BeautifulSoup(html, "html.parser")

# %%
# NOTE - Get title from Site
# body > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
my_titles = soup.select("body > div > div.table-responsive > table > tbody > tr td > a")

for i in my_titles:
    a = re.sub(r"[\d]", "", i.text)
    if a == "":
        pass
    elif a == "\n":
        pass
    elif a == "\n\n":
        pass
    else:
        print(a)

# %%
