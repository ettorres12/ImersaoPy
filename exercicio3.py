import pandas as pd
import numpy as np

#Cria o Dataframe

print("Criando um Dataframe:\n")
df_vendas = pd.DataFrame({
    "vendedor": [1, 2, 3, 4, 5, 6, 7, 8],
    "produto": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "valor_venda": [100, np.nan, 300, np.nan, 500, 600, np.nan, 800],
    "data_venda": ["03/02", np.nan, "20/08", "25/08", np.nan, "05/09", "10/09",np.nan]

})
print(df_vendas)

#Ver quais valores das colunas estão nulos
print("\nVendo quais valores das colunas estao nulos:\n")
print(df_vendas.isnull())

#Conta quantos valores estão nulos
print("\nContando quantos valores estao nulos em cada coluna:\n")
print(df_vendas.isnull().sum())

#Substitui os valores nulos da coluna valor_venda pela mediana desses valores
print("\nSubstiituindo os valores nulos da coluna valor_venda  pela mediana desse valores:\n")
df_vendas["valor_venda"] = df_vendas["valor_venda"].fillna(df_vendas["valor_venda"].median())
print(df_vendas)

#Biblioteca de data atual
import datetime as dt

#Substitui os valores nulos da coluna data_venda pela data atual
print("\nSubstitui os valores nulos da colunda data_venda pela data do dia atual:\n")
df_vendas['data_venda'] = df_vendas['data_venda'].fillna(dt.datetime.now().strftime('%d/%m'))
print(df_vendas)