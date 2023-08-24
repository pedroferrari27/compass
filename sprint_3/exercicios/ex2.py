#funcão para definir paridade
def paridade(numero):
    if numero % 2 == 0:
        return "Par: "
    else:
        return "Ímpar: "

#numero total de inputs
MAX = 3

#inicializa a string resultado
res = ""
#inicializa o loop para input
for i in range(MAX):
    #recebe o imput de como int MAX vezes
    x = int(input())
    #verifica o input e o coloca em y no formato desejado
    y = paridade(x) + str(x) + "\n"
    res = res + y
#removendo o \n final
resfinal = res[:-1]
#imprime o resultado
print(resfinal)
    
    
#outro metodo:

#receber os numeros como uma lista
#x= list(map(int,input("digite os numeros: ").split()))

#incializar uma lista vazia
#z = []
#para cada numero,adicionar na lista o resultado 
#for i in range(MAX):
#    y = list(map(str,str(paridade(x[i]) + str(x[i]) + "/n") ) )
#    z.append(y)

#imprimir resultado completo
#for j in range(MAX):
#    print(z[j])






