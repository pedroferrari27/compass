#função para definir se é par ou não
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par :"
    else:
        return "Ímpar :"

#numero total de inputs
MAX = 3

#receber os numeros como uma lista
x= list(map(int,input("digite os numeros: ").split()))

#incializar uma lista vazia
z = []
#para cada numero,adicionar na lista o resultado 
for i in range(MAX):
    y = list(map(str,str(verificar_par_impar(x[i]) + str(x[i]) + "/n") ) )
    z.append(y)

#imprimir resultado completo
for j in range(MAX):
    print(z[j])


S
    
