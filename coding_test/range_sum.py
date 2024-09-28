#백준10986

div=input()
number=list(input())
count=0
for i in number:
    a=0
    b=1
    if sum(number[a:b])/div==0:
        count+=1