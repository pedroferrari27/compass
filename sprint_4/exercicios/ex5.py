import pandas as pd
import numpy as np


colunas = ['Nome','N1','N2','N3','N4','N5']

dataframe =  pd.read_csv('estudantes.csv',names = colunas)
dataframe =dataframe.sort_values(by='Nome')
for row in dataframe.index:
    #dataframe['Name'][row],dataframe['N1'][row], dataframe['N2'][row] dataframe['N3'][row], dataframe['N4'][row] dataframe['N5'][row]
    nome = dataframe['Nome'][row]   
    notas = np.array([dataframe['N1'][row], dataframe['N2'][row],dataframe['N3'][row],dataframe['N4'][row],dataframe['N5'][row]])
    notas = sorted(notas,reverse=True)[2:]
    media = round(np.mean(notas),2)
    print(f"Nome: {nome} Notas: [{notas[0]}, {notas [1]}, {notas[2]}] Média: {media}") 
    

# codigo em pandas




#with open("estudantes.csv","r") as arquivo:
#   linha = [] 
    #pegando cada linha do csv em uma lista
#    for lin in arquivo:
#        linha.append(lin.strip())
    #print(linha)
#    tabela = []
#    for i in linha:
#        tabela.append(list(i.split(",")))
        
    
#    tabela = sorted(tabela, key=lambda x: x[0])
   
    
#    for line in tabela:
#        nome = line[0]
#        notas = map(int,[line[1],line[2],line[3],line[4],line[5]])
#        notas = sorted(notas,reverse = True)[2:]
#        media = round(sum(notas)/3,2)
        
 #       print(f"Nome: {nome} Notas: [{notas[0]}, {notas [1]}, {notas[2]}] Média: {media}") 
    
