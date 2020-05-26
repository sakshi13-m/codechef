import math 

def primeFactors(n):
    n=int(n)
    return n%4

t=int(input())
while t:
    t=t-1
    n=int(input())
    a=list(map(primeFactors,input().split()))
    cnt=0
    b1=[n for i in range(n)]
    b2=[n for i in range(n)]
    c1=[n for i in range(n)]
    ff=n
    ft=n
    st=n
    flag=1
    for i in range(n-1,-1,-1):
        z=a[i]
        if z==0:
            ff=i
        if flag and z==2:
            ft=i
            flag=0
        elif flag==0 and z==2:
            st=ft
            ft=i
        b1[i]=ft
        b2[i]=st
        c1[i]=ff
        if z==0:
            cnt+=n-i
            
        if z==2:
            cnt+=n-min(b2[i],c1[i])
            
            
        if z%2!=0:
            f=min(b1[i],c1[i])
            if f!=n and f==c1[i]:
                cnt+=n-i
                
            elif f!=n and f==b1[i]:
                d=min(b2[i],c1[i])
                cnt+=n-i-(d-f)
            else:
                cnt+=n-i
                
    
        
    print(cnt)
