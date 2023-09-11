def calcular_valor_maximo(operadores,operandos) -> float:
    
    #utilizei um dict com as operações a serem feitas,para assim utilizar a operação quando ler o simbolo em "operandos"
    operacao = {'+': lambda x, y: x + y,'-': lambda x, y: x - y,'*': lambda x, y: x * y,'/': lambda x, y: x / y,'%': lambda x, y: x % y}

    #utilizando a função zip transformamos em uma lista de tuplas onde cada tupla esta de tal forma:
        #(operanados, operadores)
    #então aplico a operação indicada no dict operacao , que está no x[1] ,na tupla operandos
    return max(map(lambda x : operacao[x[1]](x[0][0],x[0][1]) ,zip(operandos,operadores)))
    
  


#operadores = ['+','-','*','/','+']
#operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

#b = calcular_valor_maximo(operadores, operandos)