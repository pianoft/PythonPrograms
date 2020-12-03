import requests
from bs4 import BeautifulSoup
r = requests.get('https://atcoder.jp/contests/abc144/tasks/abc144_b')
soup = BeautifulSoup(r.text, "lxml")
tags = soup.find_all('h3', text=lambda t: t and 'Sample' in t)
i, j = 1, 1
for tag in tags:
    # print(tag.find_next_sibling().text)
    # print("---------------------------------")
    if i % 2:
        f = open("Input%d" % j, "w+")
    else:
        f = open("Output%d" % j, "w+")
        j += 1
    f.write(tag.find_next_sibling().text)
    f.close()
    i += 1
