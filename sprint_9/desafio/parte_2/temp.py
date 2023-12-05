#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:23:46 2023

@author: pedro
"""

import pandas as pd
from ast import literal_eval

df = pd.read_csv('/home/pedro/Desktop/rep-compasso/compas novo/compass/sprint_9/desafio/parte_1/movies_grouped.csv')

df_nomes = df[['nomeArtista', 'profissao']]


#df_filtered = df[df['profissao'].apply(lambda x: any(item in x for item in ['actor', 'actress']))]


# Get the unique values from the nomeArtista column

actors_names = df['nomeArtista'].tolist()

# Convert each string representation of a list to an actual list
list_of_lists = [literal_eval(names_str) for names_str in actors_names]

# Flatten the list of lists into a single list of names
names = [name for sublist in list_of_lists for name in sublist]

names = set(names)

df_with_array = df.withColumn("name_array", split(df["names"], ", "))