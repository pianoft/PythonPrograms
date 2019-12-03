from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
driver = webdriver.Chrome(chrome_options=options)
driver.get(config.tmp10)
element = driver.find_element_by_class_name("js-username-field")
element.send_keys(config.tmp9)
element = driver.find_element_by_class_name("js-password-field")
element.send_keys(config.tmp8)
element.send_keys(Keys.ENTER)
print("成功")