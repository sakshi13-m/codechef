t=int(input())
for _ in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    one=ar.count(1)
    o=[]
    x=0
    if(n<7 and one>1):
        print("NO")
    else:
        for i in range(n):
            if(ar[i]==1):
                o.append(i)
        for j in range(1,len(o)):
            if(o[j]-o[j-1]<6):
                x=1
        if x==0:
            print("YES")
        else:
            print("NO")
                
        
