from selenium import webdriver
import config,time
from selenium.webdriver.common.keys import Keys
def f():
    time.sleep(1)
    return
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
##########################################################
#from here
d1 = webdriver.Chrome(chrome_options=options)
d1.get(config.urlA)
element = d1.find_element_by_name(config.tmp6)
s=config.tmp1
element.send_keys(s)
element = d1.find_element_by_name(config.tmp7)
element.send_keys(config.tmp2)
element = d1.find_element_by_id(config.urlJ)
element.click()
d1.get(config.urlC)
time.sleep(1)
d1.back()
'''
##tillhere
#from here
d2 = webdriver.Chrome(chrome_options=options)
d2.get(config.urlA)
element = d2.find_element_by_name(config.tmp6)
s=config.tmp1
element.send_keys(s)
element = d2.find_element_by_name(config.tmp7)
element.send_keys(config.tmp2)
element = d2.find_element_by_id(config.urlJ)
element.click()
##till here
d2.get(config.urlB)
d2.get(config.urlD)

d3 = webdriver.Chrome(chrome_options=options)
d3.get(config.tmp10)
element = d3.find_element_by_class_name(config.x1)
element.send_keys(config.tmp9)
element = d3.find_element_by_class_name(config.x2)
element.send_keys(config.tmp8)
element.send_keys(Keys.ENTER)
#31days
d4= webdriver.Chrome(chrome_options=options)
d4.get(config.x4)
elmnt = d4.find_element_by_id(config.x5)
elmnt.send_keys(config.x7)
f()
elmnt.send_keys(Keys.ENTER)
f()
elmnt=d4.find_element_by_id(config.x6)
f()
elmnt.send_keys(config.x3)
elmnt.send_keys(Keys.ENTER)
d4.get(config.x8)
d4.get(config.x9)
d5= webdriver.Chrome(chrome_options=options)
d5.get(config.x4)
elmnt = d5.find_element_by_id(config.x5)
elmnt.send_keys(config.x7)
f()
elmnt.send_keys(Keys.ENTER)
f()
elmnt=d5.find_element_by_id(config.x6)
f()
elmnt.send_keys(config.x3)
elmnt.send_keys(Keys.ENTER)
d5.get(config.x8)
d5.get(config.x10)
#31days
print("成功12")
while 1:
    d1.refresh()
    time.sleep(30)
'''