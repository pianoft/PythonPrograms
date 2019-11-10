from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
#options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome()
driver.get('https://www.google.com/?hl=ja')
while 1:
    time.sleep(5)
    f=open("tes.txt","w+")
    s=driver.current_url;
    tmp=s.find('tasks/')
    if tmp==-1:
        continue
    f.write(driver.current_url);
    print(driver.current_url)
    f.close()
