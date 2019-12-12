from selenium import webdriver
import config,time,random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
##########################################################
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://kleki.com/')
while 1:
    t1,t2=map(int,input().split())
    action = ActionChains(driver)
    action.move_by_offset(t1,t1)
    action.click()
    action.perform()

