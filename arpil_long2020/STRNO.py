import math as mt 
def kFactors(n, k):  
    a = list() 
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2
    
    for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
    
    if n > 2: 
        a.append(n) 
    if len(a) < k:  
        return 0
    else:
        return 1
          
    
  
t=int(input())
while t:
    t=t-1
    x, k = map(int,input().split())
    
    print(kFactors(x, k))
