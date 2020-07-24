# cook your dish here
def minimumSwaps(p):
    numSwaps = 0
    i = 0
    while(i < len(p)-1):
        if p[i] != i+1:
            t = p[i]
            p[i], p[t-1] = p[t-1], p[i]
            numSwaps += 1
        else:
            i += 1
    return numSwaps
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    p=list(map(int,input().split()))
    x=[0]*m
    y=[0]*m
    for i in range(m):
        x[i],y[i]=map(int,input().split())
    if(m==0):
        s=minimumSwaps(p)
        print(s)
    else:
        s=sorted(p)
        for i in range(1,n+1):
            if(s[i-1]!=p[i-1]):
                if i in x:
                    j=x.index(i)
                    
                    p[i-1],p[y[j]-1]=p[y[j]-1],p[i-1]
        o=minimumSwaps(p)
        print(o)
                
    
    
        
