def conta_vogais(texto:str)-> int:   
    return len(list(filter(lambda x:x =="A" or x == "E" or x =="I" or x =="O" or x =="U",texto.upper())))
    

string = "Ola mundo, este e um importante teste"
a = conta_vogais(string)
print (a)



