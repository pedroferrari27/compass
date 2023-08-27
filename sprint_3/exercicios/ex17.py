lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def divide_tres(lista):
#pegando o tamanho original da lista
    tamanho = len(lista)

#dividindo os casos, no evento de ser um lista de tamanho idivisivel por 3
#calculando o tamanho das partes
    if tamanho % 3 == 0:
        tam_parte = int(tamanho / 3)
        #fazendo a divisão em respectivas partes
        a = lista[:-(2*tam_parte)] 
        b = lista[tam_parte:-tam_parte]
        c = lista[(2*tam_parte):]
        
        return a,b,c
            
            
            
            
    if tamanho % 3 == 1:
        tam_parte = int(tamanho/3)
        #como háverá uma parte maior,teremos que tratalá, colocando as divisões maiores primeiro 
        tam_parte_maior = tam_parte +1
        #fazendo a divisão em respectivas partes
        a = lista[:-(tam_parte*2)] 
        b = lista[tam_parte_maior:-tam_parte]
        c = lista[(tam_parte_maior+tam_parte):]
        
        return a,b,c
    if tamanho % 3 == 2:
        tam_parte = int(tamanho/3)
        #como háverá uma parte maior,teremos que tratalá, colocando as divisões maiores primeiro 
        tam_parte_maior = tam_parte +1
        #fazendo a divisão em respectivas partes
        a = lista[:-(tam_parte_maior+tam_parte)] 
        b = lista[tam_parte_maior:-tam_parte]
        c = lista[(tam_parte_maior*2):]
        
        return a,b,c
    

a , b, c = divide_tres(lista)
print(a,b,c)