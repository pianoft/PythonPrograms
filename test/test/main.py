n=int(input())
state=0;
for i in range(1,10):
    for j in range(2,10):
        t=i*j
        if t==n:state=1


print("Yes"if state else "No")
