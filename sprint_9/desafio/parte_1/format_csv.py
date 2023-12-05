#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:52:30 2023

@author: pedro
"""
import boto3
import pandas as pd
from datetime import datetime
from io import StringIO

#donwloada and open file
aws_access_key_id = 'AKIAZIW2UFDNKW3PZDP6'
aws_secret_access_key = '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'
bucket_name = 'raw-zone-compasso'
s3_file_key = 'raw-zone-compasso/Raw/Local/CSV/Movies/26|10|23/movies.csv'
local_file_path = '/home/pedro/Desktop/rep-compasso/compas novo/compass/sprint_8/desafio_2/testes_de_produção/movies.csv'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Download the original movies csv
try:
    s3.download_file(bucket_name, s3_file_key, local_file_path)
    print(f"Downloaded {s3_file_key} from S3 bucket to {local_file_path}")
except Exception as e:
    print(f"Error: {e}")


with open(local_file_path,"r") as arquivo:
    df = pd.read_csv(arquivo,delimiter= '|',low_memory=False)



#get id of the movies for search

generos = ['Drama', 'War']

df = df[df['genero'].str.contains('|'.join(generos))]

groups = df.groupby('id').agg({
    'tituloPincipal': 'first',
    'tituloOriginal': 'first',
    'anoLancamento': 'first',
    'tempoMinutos': 'first',
    'genero': 'first',
    'notaMedia': 'first',
    'numeroVotos': 'first',
    'generoArtista': list,
    'personagem': list,
    'nomeArtista': list,
    'anoNascimento': list,
    'anoFalecimento': list,
    'profissao': list,
    'titulosMaisConhecidos': list
}).reset_index()

# Add a new column 'count' representing the number of rows in each group
groups['countActors'] = df.groupby('id').size().reset_index(name='countActors')['countActors']

#format to csv for upload

csv_buffer = StringIO()
groups.to_csv(csv_buffer, index=False)
movies_grouped = groups.to_csv('/home/pedro/Desktop/rep-compasso/compas novo/compass/sprint_9/desafio/parte_1/movies_gouped.csv', index=False)


#receber data atual
current_datetime = datetime.now()
formatted_date = current_datetime.strftime('%y/%m/%d')
target_file =f"raw-zone-compasso/Raw/Local/CSV/Movies/{formatted_date}/movies_grouped.csv"


# upload the original movies csv
try:
    s3.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=target_file)
    print(f"uploaded file to S3 bucket on {target_file}")
except Exception as e:
    print(f"Error: {e}")

 


