from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'})
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://pdf2jpg.net/')
element=driver.find_element_by_id("advanced_pdf_file")
element.click().send_keys("Pycharm")

