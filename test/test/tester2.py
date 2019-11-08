import requests
from bs4 import BeautifulSoup
a=['a','b','c','d','e','f']
n=[-1 for i in range(6)]
for i in range(6):
    r = requests.get('https://atcoder.jp/contests/abc144/tasks/abc144_'+a[i])
    soup = BeautifulSoup(r.text,"lxml")
    tags = soup.find_all('h3', text=lambda t: t and 'Sample' in t)
    k,j=1,1
    print("length is "+str(len(tags)))
    for tag in tags:
        #print("---------------------------------")
        if k%2:
            f = open(a[i].capitalize()+"in%d" % j,"w+")
        else:
            f = open(a[i].capitalize()+"out%d" % j, "w+")
            j += 1
        f.write(tag.find_next_sibling().text )
        f.close()
        k += 1
    n[i] = int(len(tags)/2)