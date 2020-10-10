import requests
from bs4 import BeautifulSoup

req = requests.get('https://nyaa.si')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'body > div > div.table-responsive > table > tbody > tr > td:nth-child(2) > a'
)

# body > div > div.table-responsive > table > tbody > tr:nth-child(4) > td:nth-child(2) > a

mg = soup.select(
    'body > div > div.table-responsive > table > tbody > tr > td:nth-child(3) > a:nth-child(2)')
# body > div > div.table-responsive > table > tbody > tr:nth-child(4) > td:nth-child(3) > a:nth-child(2)

print(mg[0])
