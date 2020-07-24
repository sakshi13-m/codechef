# cook your dish here
t=int(input())
for _ in range(t):
    x,y,l,r = map(int,input().split())
    '''m=[]
    for z in range(r+1):
        m.append((x&z)*(y&z))
    print(l+m.index(max(m)))
    
    
    for _ in range(int(input())) :
    n, k = [int(i) for i in input().strip().split()]
    print(k-1 if (k-1)|k <= n else k-2)
    '''
    #print(bin(x).count(1))
    s=x|y
    if(x==0 or y==0):
        print(0)
    
    elif(s<=r and s>=l):
        print(s)
    else:
        #s=(x^y)+(x&y)
        for i in range(r):
            s-=pow(2,i)
            if(s<=r and s>=l):
                print(s)
            else:
                s=x|y
