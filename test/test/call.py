import os
import tester2
n = tester2.n
myCmd='python main.py < In'
a=[0 for i in range(0,n+1)]
for i in range(1,n+1):
    os.system(myCmd+str(i)+' > Submission'+str(i))
    x1 = open("Out"+str(i),"r").read()
    y1 = open("Submission"+str(i),"r").read()
    a[i]= (x1==y1)
if sum(a) < n:
    os.system("mpg123 " + ("wa.mp3") + " &")
else:
    os.system("mpg123 " + ("ac.mp3") + " &")
    print("All Green!")
for i in range(1,n+1):
    if a[i]==0:
        print("WA at Input"+str(i))
        print(open("Out"+str(i),"r").read())
        print("---Below your output.")
        open("Submission" + str(i), "r").read()

    else:
        print("AC")
