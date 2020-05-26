# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    for i in range(n):
        a=[0]*m
        a=list(map(int,input().split()))
        M=0
        m1=0
        for j in range(m):
            if(a[j]>M):
                m1=j+1
                M=a[j]
        print(m1,end=" ")
    print()
