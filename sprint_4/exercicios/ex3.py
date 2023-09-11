
import functools


def calcula_saldo(lancamentos) -> float:
    
    return functools.reduce(lambda x,y : x + y ,map(lambda x : -x[0] if x[1] != "C"  else x[0],lancamentos))
    
    
    
 
#lancamentos = [
#        (200,'D'),
#        (300,'C'),
#        (100,'C'),
#        (400,'C')
#    ]

#a = calcula_saldo(lancamentos)