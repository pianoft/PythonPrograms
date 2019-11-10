from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
#options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
# use local driver
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.google.com/?hl=ja')
driver.current_url