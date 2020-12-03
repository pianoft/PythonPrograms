from selenium import webdriver
import time
import os
import cv2
import requests
import urllib
import config
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option(
    'prefs', {'intl.accept_languages': 'en_US'})  # locale=en_US
##########################################################
driver1 = webdriver.Chrome(chrome_options=options)
driver2 = webdriver.Chrome(chrome_options=options)
driver1.get('https://atcoder.jp/contests/abc145/submissions/me')
element = driver1.find_element_by_id("username")
element.send_keys(config.USERNAME)
element = driver1.find_element_by_id("password")
element.send_keys(config.PASSWORD)
element = driver1.find_element_by_id("submit")
element.click()
driver1.minimize_window()
##########################################################################################
driver2.get('https://atcoder.jp/contests/abc145/submissions/me')
element = driver2.find_element_by_id("username")
element.send_keys(config.USERNAME)
element = driver2.find_element_by_id("password")
element.send_keys(config.PASSWORD)
element = driver2.find_element_by_id("submit")
element.click()
driver2.get('https://atcoder.jp/contests/abc145/tasks')
# 3
f = open("abc.txt", "w")
f.write("0")
f.close()
url = ""
state = 0
ac, wa, ce, tle, mle, = 0, 0, 0, 0, 0
sum = 0


def func():
    global ac, wa, tle, mle, sum, ce
    s = driver1.page_source
    state = 0
    if ac != s.count("Accepted"):
        print("AC")
        ac += 1
        state = 1
    if wa != s.count("Wrong Answer"):
        print("WA")
        wa += 1
        state = 1
    if tle != s.count("Time limit Exceeded"):
        print("TLE")
        tle += 1
        state = 1
    if ce != s.count("Compile Error"):
        print("CE")
        ce += 1
        state = 1
    if sum == ac + wa + tle + ce:
        print("変更無し")
    sum = ac + wa + tle
    return


func()
while 1:
    time.sleep(1)
    func()
    f = open("tes.txt", "w+")
    s = driver2.current_url
    tmp = s.find('tasks/')
    f2 = open("abc.txt", "r").read()
    time.sleep(1)
    t = ""
    if tmp != -1:
        length = (s.index("tasks"))
        for j in range(length):
            t += s[j]
        t += "submissions/me"
        url = t
    if int(f2) == int(1):
        f2 = open("abc.txt", "w+")
        f2.write("0")
        f2.close()
        element = driver2.find_element_by_id("input-open-file")
        element.send_keys(os.getcwd()+"/main.py")
        element = driver2.fin
        element.send_keys("Python3")
        element.click()
        element = driver2.find_element_by_id("submit")
        element.click()
    else:
        print("提出不可")
    if tmp == -1:
        continue
    f.write(driver2.current_url)
    print(driver2.current_url)
