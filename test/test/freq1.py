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
driver2 = webdriver.Chrome(chrome_options=options)
driver2.get(config.urlA)
element = driver2.find_element_by_name(config.tmp6)
s=config.tmp1
element.send_keys(s)
element = driver2.find_element_by_name(config.tmp7)
element.send_keys(config.tmp2)
element = driver2.find_element_by_id('btn')
element.click()
driver2.get(config.urlC)
##till here
#from here
driver1 = webdriver.Chrome(chrome_options=options)
driver1.get(config.urlA)
element = driver1.find_element_by_name(config.tmp6)
s=config.tmp1
element.send_keys(s)
element = driver1.find_element_by_name(config.tmp7)
element.send_keys(config.tmp2)
element = driver1.find_element_by_id('btn')
element.click()
##till here
driver1.get(config.urlB)
driver1.get(config.urlD)




driver = webdriver.Chrome(chrome_options=options)
driver.get(config.tmp10)
element = driver.find_element_by_class_name(config.x1)
element.send_keys(config.tmp9)
element = driver.find_element_by_class_name(config.x2)
element.send_keys(config.tmp8)
element.send_keys(Keys.ENTER)
print("成功2")
while 1:
    driver2.refresh()
    time.sleep(30)