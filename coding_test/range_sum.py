#백준10986

div=input(int())
number=list(map(int,input()))
count=0
for (a,i) in range(len(number)):
    if sum(number[a:i])/div==0:
        count+=1
print(count)