import os
import tester
import time
n=tester.n
os.system('g++ main.cpp')
myCmd='./a.out < '+'in'
a=[0 for i in range(0,n+1)]
for i in range(1,n+1):
    s='submission'+str(i)
    print(s)
    start_time=time.time()
    elapsed_time=time.time()-start_time;

    os.system(myCmd+str(i)+' > '+s)
    x1 = open("out"+str(i),"r").read()
    y1 = open("submission"+str(i),"r").read()
    a[i]= (x1==y1)
if sum(a) < n:
    os.system("mpg123 " + ("wa.mp3") + " &")
else:
    os.system("mpg123 " + ("ac.mp3") + " &")
    print("All Green!")
for i in range(1,n+1):
    if a[i]==0:
        print("WA at Input"+str(i))
        print(open("out"+str(i),"r").read())
        print("---Below your output.")
        open("submission" + str(i), "r").read()
    else:
        print("AC")
