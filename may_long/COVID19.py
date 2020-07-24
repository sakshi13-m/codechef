t=int(input())
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    c=1
    positive=[]
    if(n==2 and x[0]-x[1]>2):
        print(c,n-c)
    else:
        for i in range(1,n):
            if(x[i]-x[i-1]<=2):
                c+=1
            else:
                positive.append(c)
                c=1
        positive.append(c)
        if(n==c):
            print(n,n)
        else:
            print(min(positive),max(positive))
