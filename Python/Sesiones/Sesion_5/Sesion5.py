import pandas as pd
#se usa para importar bloques de datos, solo los necesarios, modulo propio de python
import chunk
#se usa para importar expresiones regulares, modulo propio de python
import re

#leer CSV (df significa dataframe)
#no ponemos ruta para coger archivo pokemo al estar en la misma carpeta que este archivo
#en dtype debemos poner el nombre exacto de la columna que nos querenmos traer
#con dtype forzamos el tipo y es opcional usarlo
pokemon_csv_df = pd.read_csv('pokemon_data.csv',
                         dtype={
                           "Name": str,
                           "Type 1" : str,
                           "Speed": int,
                           "Generation" : int
                         })
#leer de un excel
  #pokemon_excel_df = pd.read_excel('pokemon_data.xlsx')
#leer de un txt, hay que averiguar la delimitacion del archivo para indicarlo en delimiter, en este caso es una tabulacion
  #pokemon_txt_df = pd.read_csv('pokemon_data.txt', delimiter = '\t')

#imprimir los valores
  #print(pokemon_csv_df)

#imprimir 5 primeros
  #print(pokemon_csv_df.head(5))

#imprimir los 5 ultimos
  #print(pokemon_csv_df.tail(5))

#obtener nombres de columnas
  #print(pokemon_csv_df.columns)

#obtener todos los nombres
  #nombres = pokemon_csv_df['Name']
  #print(nombres)

#obtener todos los nombres y sus velocidades
  #nombres_velocidades= pokemon_csv_df[['Name', 'Speed']]
  #print(nombres_velocidades)

#obtener todos los nombres y sus velocidades v2
  #lista_columnas = ['Name', 'Speed']
  #nombres_velocidades= pokemon_csv_df[lista_columnas]
  #print(nombres_velocidades)

#obtener los primeros 5 nombres
  #primeros_5 = pokemon_csv_df['Name'][0:5]
  #print(primeros_5)

#obtener todas la primera fila
  #print(pokemon_csv_df.iloc[0])

#obtener las 3 primeras filas
print(pokemon_csv_df.iloc[0:3])