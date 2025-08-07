import pandas as pd

import numpy as np

# Criação de um DataFrame de exemplo com valores nulos na coluna 'salario'
df_salarios = pd.DataFrame({
    'nome': ['Joao', 'Maria', 'Pedro', 'Ana'],
    'salario': [5000, np.nan, 7000, np.nan],
})

# Preenche os valores nulos com a média dos salários (arredondada) e armazena em nova coluna
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

# Preenche os valores nulos com a mediana dos salários e armazena em nova coluna
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

print("\nDataFrame com salario preenchido por media e mediana:")
print(df_salarios)

print("\n\nCria mais um Dataframe como exemplo")

df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'],
    'temperatura': [30, np.nan, np.nan, 33, 31]
})

# ffill: preenche os nulos com o valor anterior
df_temperaturas['preenchido_ffil'] = df_temperaturas['temperatura'].ffill()

print("\nDataFrame com preenchimento ffill (valor anterior):")
print(df_temperaturas)

# bfill: preenche os nulos com o valor posterior
df_temperaturas['preenchido_bfil'] = df_temperaturas['temperatura'].bfill()

print("\nDataFrame com preenchimento bfill (valor posterior):")
print(df_temperaturas)

# Criação de DataFrame com nomes e cidades (com valores ausentes)
print("\n\n Cria mais um DataFrame de exemplo")
df_cidades = pd.DataFrame({
    'nome': ['Joao', 'Maria', 'Pedro', 'Ana'],
    'cidade': ['Sao Paulo', np.nan, 'Belo Horizonte', np.nan]
})

# Preenche os valores ausentes com a string "Nao informada"
df_cidades["cidade"] = df_cidades['cidade'].fillna('Nao informada')

print("\nDataFrame com cidade preenchida com texto fixo:")
print(df_cidades)

