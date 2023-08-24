def palindromo(a):
    #utilizando a string ae elendo ela com a[::-1], pegamos a string invertida, e depois comparamos ela com a original para ver se é palindromo 
    if a[::-1] == a:
        return True
    else :
        return False


palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] 

for i in range(len(palavras)):
    if palindromo(palavras[i]) == True :
        res = "A palavra: "+ str(palavras[i]) +" é um palíndromo"
        print(res)
    else :
        res = "A palavra: "+ str(palavras[i]) +" não é um palíndromo"
        print(res)