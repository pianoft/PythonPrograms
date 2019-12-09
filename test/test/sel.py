from selenium import webdriver
import time,os,cv2,requests,urllib
import config
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
##########################################################
driver1 = webdriver.Chrome(chrome_options=options)
driver2 = webdriver.Chrome(chrome_options=options)
driver1.get('https://atcoder.jp/contests/abc145/submissions/me')
element = driver1.find_element_by_id("username")
element.send_keys(config.USERNAME)
element = driver1.find_element_by_id("password")
element.send_keys(config.PASSWORD)
element = driver1.find_element_by_id("submit")
element.click()
driver1.minimize_window()
##########################################################################################
driver2.get('https://atcoder.jp/contests/abc145/submissions/me')
element = driver2.find_element_by_id("username")
element.send_keys(config.USERNAME)
element = driver2.find_element_by_id("password")
element.send_keys(config.PASSWORD)
element = driver2.find_element_by_id("submit")
element.click()
driver2.get('https://atcoder.jp/contests/abc145/tasks')
##########################################################3
f = open("abc.txt", "w")
f.write("0")
f.close()
url=""
state=0;
ac,wa,ce,tle,mle,=0,0,0,0,0
sum=0
def init():
    global ac, wa, tle, mle, sum, ce
    s = driver1.page_source
    ac = s.count("Accepted")
    wa = s.count("Wrong Answer")
    ce = s.count("Compilation Error")
    tle = s.count("Time limit Exceeded")
    sum = ac+wa+ce+tle
    return
def func():
    global ac,wa,tle,mle,sum,ce
    s = driver1.page_source
    state = 0;
    if ac != s.count("Accepted"):
        print("AC")
        ac += 1
        os.system("mpg123 " + ("AC.mp3") + " &")
        os.system("cp main2.cpp yobi.cpp")
        os.system("cp new.cpp main2.cpp")
        state = 1;
    if wa != s.count("Wrong Answer"):
        print("WA")
        wa += 1
        os.system("mpg123 " + ("WA.mp3") + " &")
        state = 1;
    if tle != s.count("Time limit Exceeded"):
        print("TLE")
        tle += 1
        os.system("mpg123 " + ("TLE.mp3") + " &")
        state = 1;
    if ce != s.count("Compilation Error"):
        print("CE")
        ce += 1
        os.system("mpg123 " + ("CE.mp3") + " &")
        state = 1;
    if sum == ac + wa + tle + ce:
        nothing_has_changed=1
    sum = ac + wa + tle +ce
    print("ac:"+str(ac)+","+"wa:"+str(wa)+","+"ce:"+str(ce)+","+"tle:"+str(tle))
    return
init()
while 1:
    driver1.refresh()
    time.sleep(2)
    func()
    f=open("tes.txt","w+")
    s = driver2.current_url
    tmp = s.find('tasks/')
    f2 = open("abc.txt", "r").read()
    time.sleep(1)
    t = ""
    if tmp!=-1:
        length = (s.index("tasks"))
        for j in range(length):
            t += s[j]
        t += "submissions/me"
        url=t
    if int(f2) == int(1):
        f2=open("abc.txt","w+")
        f2.write("0")
        f2.close()
        element=driver2.find_element_by_id("input-open-file")
        element.send_keys(os.getcwd()+"/main2.cpp")
        element=driver2.find_element_by_id("submit")
        element.click()
    if tmp==-1:
        continue
    f.write(driver2.current_url);
    print(driver2.current_url)