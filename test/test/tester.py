import requests
from bs4 import BeautifulSoup
s=open("tes.txt","r").read()
r = requests.get(s)
soup = BeautifulSoup(r.text,"lxml")

tags = soup.find_all('h3', text=lambda t: t and 'Sample' in t)

if len(tags)==0:
    tags = soup.find_all('h3', text=lambda t: t and '例' in t)

k,j=1,1
for tag in tags:
    if k%2:
        f = open("in%d"% j,"w+")
    else:
        f = open("out%d"% j,"w+")
        j += 1
    f.write(tag.find_next_sibling().text )
    f.close()
    k += 1
n = int(len(tags)/2)