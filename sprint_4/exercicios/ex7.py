def pares_ate(n:int):
    if n >= 2:    
        for k in range(2, n + 1, 2):
            yield k
    else:
       yield []
            

#j = 9            
#k = pares_ate(j)


#for i in k:
#    print(i)