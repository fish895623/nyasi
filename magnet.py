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
r = re.compile(r"^[^\/]")
for i in my_titles:
    if r.search(i['href']) == None:
        pass
    else:
        print(i['href'])
# %%
