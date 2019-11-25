import requests,urllib
from bs4 import BeautifulSoup
import http.cookiejar, urllib.request
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
username,password = '',''
postdata = {'name': username, 'password': password }
encoded_postdata = urllib.parse.urlencode(postdata).encode('utf-8')
req = opener.open("https://arc001.contest.atcoder.jp/login",encoded_postdata)
#print(req.read().decode('utf-8')) # req.read()だけだとバイナリで表示されてよくわからないのでutf8の文字列に変換
req = opener.open("https://arc001.contest.atcoder.jp/submissions/me")
soup = BeautifulSoup(req,"html.parser")
tags = soup.find_all('li')
for tag in tags:
    print(tag)