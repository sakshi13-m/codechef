# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if(n==1):
        print(1)
        print("1 1")
    else:
        print(n//2)
        for i in range(0,(n//2)):
            if(n%2==1 and i==0):
                print(str(3)+" "+str(i*2+1)+" "+str(i*2+2)+" "+str(n))
            else:
                print(str(2)+" "+str(i*2+1)+" "+str(i*2+2))
