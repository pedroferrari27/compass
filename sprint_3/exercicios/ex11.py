
temp = []
with  open("arquivo_texto.txt", "r") as arquivo:
    for linha in arquivo:
        #print(linha.strip())
        temp.append(linha.strip())
        
    arquivo.close()   
#manobra para retirar o \n
print(temp[0] + "\n" + temp[1] + "\n" + temp[2] + "\n" + temp[3],end="")
