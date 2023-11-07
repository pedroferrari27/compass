import random
import csv

# Criar uma lista com 250 inteiros aleatórios
lista = [random.randint(1, 100)for i in range(250)]

# Aplicar o método reverse para inverter a ordem dos elementos
lista.reverse()

# Imprimir a lista invertida
print(lista)

animais = ["Cachorro", "Gato", "Elefante", "Leão", "Girafa", "Tigre", "Rinoceronte", "Urso", "Zebra", "Cavalo", "Papagaio", "Gorila", "Camelo", "Pinguim", "Canguru", "Hipopótamo", "Serpente", "Macaco", "Coelho", "Avestruz"]

animais.sort()

for animal in animais:
    print(animal)


# Nome do arquivo CSV
nome_arquivo = "animais.csv"

# Abra o arquivo no modo de escrita
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # Escreva cada animal em uma linha no arquivo CSV
    for animal in animais:
        escritor_csv.writerow([animal])

print(f'Os animais foram salvos em "{nome_arquivo}" no formato CSV.')
