from selenium import webdriver
import time
import config
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
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
ac,wa,tle,mle,=0,0,0,0
sum=0
