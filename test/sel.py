from selenium import webdriver
from bs4 import BeautifulSoup
import time,os,requests
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
#options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://atcoder.jp/contests/abc144/tasks/abc144_b')
f = open("abc.txt", "w")
f.write("0")
f.close()

while 1:
    time.sleep(3)
    f=open("tes.txt","w+")
    s=driver.current_url;
    tmp=s.find('tasks/')
    f2 = open("abc.txt", "r").read()
    if int(f2) == 1:
        print("おめ!")
        element=driver.find_element_by_id("input-open-file")
        element.send_keys(os.getcwd()+"/main.cpp")
        element=driver.find_element_by_id("submit")
        #element.click()
        r = requests.get("https://atcoder.jp/contests/abc144/submissions/me")
        soup = BeautifulSoup(r.text, "lxml")
        tags = soup.find_all('class', text=lambda t: t and 'no-break' in t)
        print(len(tags))
        time.sleep(10)
        f2=open("abc.txt","w+")
        f2.write("0")
    else:
        print("ぽよ")
    if tmp==-1:
        continue
    f.write(driver.current_url);
    print(driver.current_url)
