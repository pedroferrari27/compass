primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
    
for i in range(len(idades)):
    res =  str(i) + " - " + str(primeirosNomes[i]) + " " + str(sobreNomes[i]) + " está com " + str(idades[i]) + " anos" 
    print(res)


#Você deve Utilizar a função enumerate().