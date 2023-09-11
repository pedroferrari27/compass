def maiores_que_media(conteudo:dict)->list:
    lista = list(conteudo.items())
    mean = 0
    for tupla in lista:
        mean += tupla[1]
    mean = mean/len(lista)
    lista = list(filter(lambda x : x[1] > mean , lista))
    lista = sorted(lista,key = lambda x: x[1])
    
    return lista















#conteudo = {
#    "arroz": 4.99,
#    "feijão": 3.49,
#    "macarrão": 2.99,
#    "leite": 3.29,
#    "pão": 1.99
#}

#k = maiores_que_media(conteudo)
