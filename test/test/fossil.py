import urllib.request
import http.cookiejar, urllib.request
from bs4 import BeautifulSoup
cj = http.cookiejar.CookieJar()
opener= urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
req=opener.open("https://atcoder.jp/contests/abc144/tasks/abc144_e")
soup=BeautifulSoup(req,"lxml")
tags=soup.select('pre')
#\r.carriage return.It bring the carsol to the leftmost postition.
#\n.linefeeding
f = open("input.txt", "w+")
idx=0;
i=1;
n=int(len(tags))
m=int(n/2)
for tag in tags:
    if idx==0:
        idx+=1
        i+=1
        continue
    f.write(tag.text.strip()+"\n")
    if i==m:
        break
    i+=1
f = open("input.txt", "r")
rows=f.readlines()
for row in rows:
    a=list(map(int,row.split(" ")))
    print(a)
f.close()
print(m)