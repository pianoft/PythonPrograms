from selenium import webdriver
import time,os,cv2,requests,urllib
import config
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
##########################################################

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.com/")
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

'''
for i in range(0,30):
    print("Input the value.")
    n=int(input())
    handles = driver.window_handles  # 状況を更新する
    driver.switch_to_window(handles[n])#遷移する
    print(driver.current_url)#遷移後の現在URL
    #0,n,n-1,n-2,n-3,....,1となる.
    #iが小さい程,新しく開かれてる.
'''
