from selenium import webdriver
import time,os
import cv2
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://atcoder.jp/contests/abc145')
f = open("abc.txt", "w")
f.write("0")
f.close()
while 1:
    time.sleep(1)
    f=open("tes.txt","w+")
    s = driver.current_url
    tmp = s.find('tasks/')
    f2 = open("abc.txt", "r").read()
    t = ""
    if tmp==1:
        length = (s.index("tasks"))
        for j in range(length):
            t += s[j]
        t += "submissions/me"
        #driver.implicitly_wait(10)
#    driver.get(t)
 #   driver.get_screenshot_as_file(os.getcwd() + "/former.png")
 #   driver.get(s)
    if int(f2) == int(1):
        f2=open("abc.txt","w+")
        f2.write("0")
        f2.close()
        element=driver.find_element_by_id("input-open-file")
        element.send_keys(os.getcwd()+"/main.cpp")
        element=driver.find_element_by_id("submit")
        element.click()
        time.sleep(5)
    else:
        print("提出不可")
    if tmp==-1:
        continue
    f.write(driver.current_url);

    print(driver.current_url)
