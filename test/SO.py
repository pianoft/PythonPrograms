from selenium import webdriver
import time,os
import cv2
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
#options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://atcoder.jp/contests/abc144/tasks/abc144_b')

