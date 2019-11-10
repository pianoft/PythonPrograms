from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com')
f=open("current_url.txt","w+")
f.write(driver.current_url);
f.close()
