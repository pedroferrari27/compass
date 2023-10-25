import pandas as pd
import numpy as np



with open("actors.csv","r") as arquivo:
    df = pd.read_csv(arquivo)

#ex1

maior_numero_filmes = df.loc[df['Number of Movies'].idxmax()]

print("o ator/atriz com maior número de filmes é " + str(maior_numero_filmes['Actor']) +  " com " + str(maior_numero_filmes['Number of Movies']) + " filmes.")

#ex 2

media_filmes = df['Number of Movies'].mean()

print("O numero médio de filmes é " + str(media_filmes))

#ex 3

maior_media = df.loc[df['Average per Movie'].idxmax()]

print("o ator/atriz com maior media por filme é " + str(maior_media['Actor']) +  " com " + str(maior_media['Average per Movie']) + " de  filmes.")

#ex 4

frequencia = df['#1 Movie'].value_counts()
nome_maior_frequencia = frequencia.idxmax()
maior_frequencia = frequencia[nome_maior_frequencia]

print("O filme mais frequente é " + str(nome_maior_frequencia) + " com " + str(frequencia[nome_maior_frequencia]) + " aparições na lista")