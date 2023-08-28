
import json

dicionario = {}

with open("person.json", "r") as arquivo:
    dados = arquivo.read()
    dicionario = json.loads(data)

print(dicionario)



#tentativa sem importar json

#with  open("person.json", "r") as arquivo:
#    dicionario = {}
#    temp = []
#    for linha in arquivo:
     #  dicionario.update(linha.strip().format_map())
       #print(linha.strip())
#       temp.append(linha.strip())
       
#    for i in range (1,len(temp)-1):
      
#       a = temp[i].strip(",").strip()
#       b,c = a.split(":",1)
#       dicionario.update({b:c})
     #print(dicionario)    


#porem não consegui colocar em um formato que a udemy aceita