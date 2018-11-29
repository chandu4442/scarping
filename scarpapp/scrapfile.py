import requests
from bs4 import BeautifulSoup
page=requests.get('https://en-gb.facebook.com/login/')
soup=BeautifulSoup(page.content,'html.parser')
print(soup.select('title'))

