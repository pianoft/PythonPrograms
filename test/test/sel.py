from selenium import webdriver
import time,os,cv2,requests,urllib
import config
options = webdriver.ChromeOptions()
options.add_argument('--incognito')  # secret mode
options.add_experimental_option('prefs', {'intl.accept_languages': 'en_US'}) # locale=en_US
##########################################################
judgement_window = webdriver.Chrome(chrome_options=options)
TargetProblemWindow = webdriver.Chrome(chrome_options=options)
judgement_window.get('https://atcoder.jp/contests/abc147/submissions/me')
elmnt = judgement_window.find_element_by_id("username")
elmnt.send_keys(config.USERNAME)
elmnt = judgement_window.find_element_by_id("password")
elmnt.send_keys(config.PASSWORD)
elmnt = judgement_window.find_element_by_id("submit")
elmnt.click()
judgement_window.minimize_window()
##########################################################################################
TargetProblemWindow.get('https://atcoder.jp/contests/abc147/submissions/me')
elmnt = TargetProblemWindow.find_element_by_id("username")
elmnt.send_keys(config.USERNAME)
elmnt = TargetProblemWindow.find_element_by_id("password")
elmnt.send_keys(config.PASSWORD)
elmnt = TargetProblemWindow.find_element_by_id("submit")
elmnt.click()
TargetProblemWindow.get('https://atcoder.jp/contests/abc147/tasks')
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
    s = judgement_window.page_source
    ac = s.count("Accepted")
    wa = s.count("Wrong Answer")
    ce = s.count("Compilation Error")
    tle = s.count("Time Limit Exceeded")
    sum = ac+wa+ce+tle
    return
def func():
    global ac,wa,tle,mle,sum,ce
    s = judgement_window.page_source
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
    if tle != s.count("Time Limit Exceeded"):
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
    judgement_window.refresh()
    time.sleep(0.5)
    f=open("tes.txt","w+")
    s = TargetProblemWindow.current_url
    tmp = s.find('tasks/')
    f2 = open("abc.txt", "r").read()
    time.sleep(0.5)
    t = ""
    if tmp!=-1:
        length = (s.index("tasks"))
        for j in range(length):
            t += s[j]
        t += "submissions/me"
        url=t
        if url != judgement_window.current_url:
            print("変更あり　変更あり　変更あり　変更あり　変更あり　")
            judgement_window.get(url)
            init()
    if int(f2) == int(1):
        f2=open("abc.txt","w+")
        f2.write("0")
        f2.close()
        elmnt=TargetProblemWindow.find_element_by_id("input-open-file")
        elmnt.send_keys(os.getcwd() + "/main2.cpp")
        elmnt=TargetProblemWindow.find_element_by_id("submit")
        elmnt.click()
    if tmp==-1:
        continue
    func()
    f.write(TargetProblemWindow.current_url)
    print(TargetProblemWindow.current_url)