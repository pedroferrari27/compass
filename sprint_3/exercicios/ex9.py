primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'Jos�']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
    
for i in range(len(idades)):
    res =  str(i) + " - " + str(primeirosNomes[i]) + " " + str(sobreNomes[i]) + " est� com " + str(idades[i]) + " anos" 
    print(res)


#Voc� deve Utilizar a fun��o enumerate().