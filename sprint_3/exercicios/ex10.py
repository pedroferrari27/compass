a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
#trasnformando em um set, as repetiçoes são eliminadas, pois um set não permite elementos repetidos 
setA = set(a)

#transformando novamente em lista
b = list(setA) 

print(b)

