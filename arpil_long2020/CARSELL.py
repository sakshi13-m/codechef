from sys import stdin
t=int(stdin.readline())
for _ in range(t):
    n=int(stdin.readline())
    pro=list(map(int,stdin.readline().split()))
    pro.sort(reverse=True)
    for i in range(len(pro)):
        if(pro[i]-i>0):
            pro[i]-=i
        else:
            pro[i]=0
        
    print(sum(pro)%1000000007)
