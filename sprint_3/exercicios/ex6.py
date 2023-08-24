a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


setA = set(a)
setB = set(b)
res = list(setA - set.difference(setA,setB))
#a funçao difference remove a intersecçao de 2 sets, assim, removendo a intersecção, temos sobrando os elementos em comum
print (res)