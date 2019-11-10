import os
import tester2
while(1):
    m=int(input())
    n=tester2.n[m-1]
    c=tester2.a[m-1].capitalize()
    myCmd='./a.out < '+c+'in'
    a=[0 for i in range(0,n+1)]
    for i in range(1,n+1):
        s=c+'submission'+str(i)
        print(s)
        os.system(myCmd+str(i)+' > '+s)
        x1 = open(c+"out"+str(i),"r").read()
        y1 = open(c+"submission"+str(i),"r").read()
        a[i]= (x1==y1)
    if sum(a) < n:
        os.system("mpg123 " + ("wa.mp3") + " &")
    else:
        os.system("mpg123 " + ("ac.mp3") + " &")
        print("All Green!")
    for i in range(1,n+1):
        if a[i]==0:
            print("WA at Input"+str(i))
            print(open(c+"out"+str(i),"r").read())
            print("---Below your output.")
            open(c+"submission" + str(i), "r").read()
        else:
            print("AC")
