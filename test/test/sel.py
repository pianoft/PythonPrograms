from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
#options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.google.com/?hl=ja')
driver.get('https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b')

while 1:
    time.sleep(5)
    f=open("tes.txt","w+")
    s=driver.current_url;
    tmp=s.find('tasks/')
    f2 = open("abc.txt", "r").read()
    if int(f2) == 1:
        print("おめ!")
    else:
        print("ぽよ")
    if tmp==-1:
        continue
    f.write(driver.current_url);
    print(driver.current_url)