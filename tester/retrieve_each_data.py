import requests
from bs4 import BeautifulSoup
r = requests.get('https://atcoder.jp/contests/abc144/tasks/abc144_f')
soup = BeautifulSoup(r.text,"lxml")
tags = soup.find_all('h3', text=lambda t: t and 'Sample' in t)
for tag in tags:
    print(tag.find_next_sibling().text)
    print("---------------------------------")