#1 - Receber uma string via input

#2 - Gerar o hash  da string por meio do algoritmo SHA-1

#3 - Imprimir o hash em tela, utilizando o método hexdigest

#4 - Retornar ao passo 1

import hashlib


while True:
  print(hashlib.sha256(input().encode()).hexdigest())

