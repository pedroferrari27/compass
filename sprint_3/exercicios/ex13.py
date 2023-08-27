def function_square(a):
    a = a * a 
    return a

    

def my_map(lista , func):
    for i in range(len(lista)):
        lista[i] = func(lista[i])
    return lista
    
    
    
    
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = my_map(lista_original,function_square)

print (res)