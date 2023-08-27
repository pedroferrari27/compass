import random

#inicializando valores
random_list = random.sample(range(500), 50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

#deixando a lista ordenada para conveniencia
random_list.sort()
#calculando valores

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = (sum(random_list)/len(random_list))
#calculo mediana
if len(random_list) % 2 == 0:
    mediana = (random_list[len(random_list)//2] + random_list[len(random_list)//2 - 1]) / 2
else:
    mediana= random_list[len(random_list)//2] 

res = "Media: "+ str(media) +", Mediana: "+ str(mediana) +", Mínimo: "+ str(valor_minimo) +", Máximo: "+ str(valor_maximo)


print(res)

