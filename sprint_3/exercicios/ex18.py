speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

lista_valores = list(speed.values())

#removendo repetiçoes transformando em set e retornando

lista_valores = set(lista_valores)
lista_valores = list(lista_valores)

print(lista_valores)

