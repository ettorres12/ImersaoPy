import pandas as pd

import numpy as np

#Cria um DataFrame chamado df_produtos com as seguintes colunas: "produto", "preco" e "quantidade_em_estoque".
print("Criando um DataFrame: ")
df_produtos = pd.DataFrame({
    'produto': ["Calca", "Blusa", "Short", "Saia", "Vestidos"],
    'preco': [150, 50, np.nan, 80, np.nan],
    'quantidade_em_estoque': [np.nan, 10, 20, 50, np.nan]
})

print("Tabela:\n", df_produtos)

#Identifica os valores nulos em cada coluna.
print("\nIdentificando os valores nulos:\n", df_produtos.isnull())

#Conta os valores nulos em cada coluna.
print("\n Contando os valores nulos nas colunas:\n", df_produtos.isnull().sum())

df_produtos[df_produtos.isnull().any(axis=1)]

#Preenche os valores nulos da coluna "preco" com a média dos preços dos produtos.
print("\nPreenchendo os valores nulos com a media dos precos dos produtos:\n")
df_produtos["preco_media"] = df_produtos["preco"].fillna(df_produtos["preco"].mean().round(2))
print(df_produtos)

#Preenche os valores nulos da coluna "quantidade_em_estoque" com o valor "0" (zero).
print("\nPreenchendo os valores nulos da coluna quantidade em estoque com 0\n")
df_produtos["quantidade_em_estoque"] = df_produtos["quantidade_em_estoque"].fillna(0)
print(df_produtos)

#Mostra as informações do dataframe
print("\nMostra as informacoes do dataframe:\n")
df_produtos.info()

#Substitui os valores nulos da coluna preco por não informado
print("\nSubstituindo os valores nulos de preco por nao informado\n")
df_produtos['preco'] = df_produtos['preco'].fillna('nao informado')
print(df_produtos)

#Exclui a coluna preco_media
df_produtos = df_produtos.drop('preco_media', axis=1)

#Muda o tipo de dados da coluna quantidade em estoque de float para int
print("\nMudando o tipo de dados de quantidade em estoque de float para int:\n")
df_produtos = df_produtos.assign(quantidade_em_estoque = df_produtos["quantidade_em_estoque"].astype("int64"))
print(df_produtos)