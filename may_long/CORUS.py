# cook your dish here
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=input()
    char_counter={}
    
    for keys in s: 
        char_counter[keys] = char_counter.get(keys, 0) + 1
    #print(char_counter)
    for i in range(q):
        x=0
        iso_ward=int(input())
        for keys in char_counter:
            if(char_counter[keys]>iso_ward):
                #print(keys)
                x=x+(char_counter[keys]-iso_ward)
        print(x)
        
