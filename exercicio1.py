# Análise do dataset Iris - Versão para rodar localmente no VS Code

import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o dataset Iris (o arquivo deve estar na mesma pasta deste script)
df = pd.read_csv('Iris.csv')

# 2. Visualizar as primeiras linhas
print("\nPrimeiras 5 linhas do DataFrame:")
print(df.head())

# 3. Informações gerais sobre o DataFrame
print("\nInformacoes do DataFrame:")
df.info()

# 4. Estatísticas descritivas das colunas numéricas
print("\nEstatisticas descritivas:")
print(df.describe())

# 5. Formato do DataFrame
print("\nFormato do DataFrame:")
print(df.shape)

# 6. Número de linhas e colunas
linhas, colunas = df.shape
print("\nO dataset possui", linhas, "linhas e", colunas, "colunas")

# 7. Nomes originais das colunas
print("\nNomes originais das colunas:")
print(df.columns)

# 8. Renomear colunas para português
renomear_colunas = {
    'Id': 'id',
    'SepalLengthCm': 'comprimento_sepala',
    'SepalWidthCm': 'largura_sepala',
    'PetalLengthCm': 'comprimento_petala',
    'PetalWidthCm': 'largura_petala',
    'Species': 'especie'
}
df.rename(columns=renomear_colunas, inplace=True)

# 9. Visualizar colunas após renomeação
print("\nDataFrame apos renomear colunas:")
print(df.head())

# 10. Contagem de valores por categoria
print("\nContagem por espécie:")
print(df['especie'].value_counts())

print("\nContagem por comprimento da pétala:")
print(df['comprimento_petala'].value_counts())

print("\nContagem por largura da pétala:")
print(df['largura_petala'].value_counts())

print("\nContagem por comprimento da sépala:")
print(df['comprimento_sepala'].value_counts())

print("\nContagem por largura da sépala:")
print(df['largura_sepala'].value_counts())

# 11. Cálculo da média das medidas por espécie
numerical_cols = ['comprimento_sepala', 'largura_sepala', 'comprimento_petala', 'largura_petala']
average_measurements = df.groupby('especie')[numerical_cols].mean()

# 12. Visualização gráfica
average_measurements.plot(kind='bar', figsize=(10, 6))
plt.title('Média das Características Numéricas por Espécie')
plt.xlabel('Espécie')
plt.ylabel('Média (Cm)')
plt.xticks(rotation=0)
plt.legend(title='Característica')
plt.tight_layout()
plt.show()
