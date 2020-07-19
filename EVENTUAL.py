# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    #n,x=map(int,input().split())
    s=input()
    d={}
    f=0
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]]+=1 
        else:
            d[s[i]]=1
    for i in d:
        if(d[i]%2!=0):
            print('NO')
            f=1
            break
    if(f==0):
        print('YES')
