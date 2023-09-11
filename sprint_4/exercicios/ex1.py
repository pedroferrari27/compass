

lista=[]
with open("number.txt","r") as arquivo:
    for line in arquivo:
        lista.append(int(line.strip()))


#filter retorna a lista com apenas pares usando função lambda, entã fazemos um sort colcando em ordem decrescente  
print(sorted(list(filter(lambda x: x % 2 == 0, map(int,lista))),reverse=True)[:5])
#e então a soma destes com sum
print(sum(map(int,sorted(list(filter(lambda x: x % 2 == 0, lista)),reverse=True)[:5])))

