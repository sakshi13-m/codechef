# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c={}
    f=0
    #count frequency of each element
    for i in range(n):
        if a[i] in c:
            c[a[i]]+=1
        else:
            c[a[i]]=1
    #check if they are unique
    if(len(set(c.values()))!=len(c.values())):
        print("NO")
        f=1
    else:
        i=0
        while(i<n):
            if a[i] in c:
                v=c[a[i]]
                #print(a[i],a[i+v-1],i,i+v-1)
                if(i+v-1<n):
                    if(a[i]==a[i+v-1] ):
                        i+=v
                    else:
                        print("NO")
                        f=1
                        break
                else:
                    f=1
                    print("NO")
                    break
    if(f==0):   
        print("YES")
