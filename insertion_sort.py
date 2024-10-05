#백준 11399, ATM인출 시간 계산하기

customers=input()
waiting=input()
time=list(map(int,waiting.split()))
n=len(time)
for i in range(n):
    for j in range(0,n-i-1):
        if time[j]>time[j+1]:
            time[j],time[j+1]=time[j+1],time[j]
mylist=[]
for i in range(n):
 mylist.append(int(time[i]*int((n-i))))
print(sum(mylist))



