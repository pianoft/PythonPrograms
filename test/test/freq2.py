from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config,time
def f():
    time.sleep(0.8)
    return
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
d1= webdriver.Chrome(chrome_options=options)
d1.get(config.x4)
elmnt = d1.find_element_by_id(config.x5)
elmnt.send_keys(config.x7)
f()
elmnt.send_keys(Keys.ENTER)
f()
elmnt=d1.find_element_by_id(config.x6)
f()
elmnt.send_keys(config.x3)
elmnt.send_keys(Keys.ENTER)
d1.get(config.x8)
