import os
import tester
import time
n=tester.n
os.system('rm ./a.out')
os.system('g++ main2.cpp')
myCmd='./a.out < '+'in'
a=[0 for i in range(0,n+1)]
state1=-1
for i in range(1,n+1):
    s='submission'+str(i)
    print(s)
    os.system(myCmd+str(i)+' > '+s)
    x1 = open("out"+str(i),"r").read()
    y1 = open("submission"+str(i),"r").read()
    a[i]= (x1==y1)
if sum(a) < n:
    state1=0;
    os.system("mpg123 " + ("wa.mp3") + " &")
else:
    os.system("mpg123 " + ("ac.mp3") + " &")
    print("All Green!")
    state1=1;
for i in range(1,n+1):
    if a[i]==0:
        print("WA at Input"+str(i))
        print(open("out"+str(i),"r").read())
        print("---Below your output.")
        dd=open("submission" + str(i), "r").read()
        print(dd)
    else:
        if state1!=1:print("AC")
f=open("abc.txt","w+");
f.write(str(state1))

