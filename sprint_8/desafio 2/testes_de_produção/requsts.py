import requests
import pandas as pd

from IPython.display import display


api_key = "f195fd8c9afef0db2bf8136e5452b574"
read_key=  "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTk1ZmQ4YzlhZmVmMGRiMmJmODEzNmU1NDUyYjU3NCIsInN1YiI6IjY1NDkyODI5NmJlYWVhMDBjOWZkNzI5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TK_o1CliJTUqQ9x_q353CkHopwkxrxb_eGK9b-ZiaEc"

url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&page=1&&with_genres=80%7C10752"



response = requests.get(url)
data = response.json()





filmes = []


for movie in data['results']:
    df = {'Titulo': movie['title'],
'Data de lançamento': movie['release_date'],
'Visão geral': movie['overview'],
'Votos': movie['vote_count'],
'Média de votos:': movie['vote_average']}


    filmes.append(df)


df = pd.DataFrame(filmes)
display(df)

with open('movies.json', 'w') as json_file:
    for _, row in df.iterrows():
        json_row = row.to_json()
        json_file.write(json_row + '\n')

#genres
#id 10752 guerra id 80 crime