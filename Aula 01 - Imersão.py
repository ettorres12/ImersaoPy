# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Lê o arquivo CSV diretamente da internet
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Visualiza as 10 primeiras linhas do DataFrame
print("\nPrimeiras 10 linhas do DataFrame:")
print(df.head(10))

# Mostra informações sobre os tipos de dados e valores nulos
print("\nInformacoes do DataFrame:")
df.info()

# Exibe estatísticas descritivas das colunas numéricas
print("\nEstatisticas descritivas das colunas numericas:")
print(df.describe())

# Mostra o número de linhas e colunas da base
print("\nFormato do DataFrame (linhas, colunas):")
print(df.shape)

# Armazena o número de linhas e colunas separadamente
linhas, colunas = df.shape[0], df.shape[1]

# Exibe o número de linhas e colunas
print("\nNumero de linhas:", linhas)
print("\nNumero de colunas:", colunas)

# Mostra os nomes das colunas originais
print("\nColunas originais:")
print(df.columns)

# Dicionário para renomear as colunas para nomes em português
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

# Renomeia as colunas usando o dicionário acima
df.rename(columns=renomear_colunas, inplace=True)

# Exibe os novos nomes das colunas
print("\nColunas apos renomeacao:")
print(df.columns)

# Contagem de valores por nível de senioridade
print("\nContagem de valores por senioridade:")
print(df["senioridade"].value_counts())

# Contagem de valores por tipo de contrato
print("\nContagem de valores por tipo de contrato:")
print(df["contrato"].value_counts())

# Contagem de valores por regime de trabalho remoto
print("\nContagem de valores por tipo de trabalho (remoto):")
print(df["remoto"].value_counts())

# Contagem de valores por tamanho da empresa
print("\nContagem de valores por tamanho da empresa:")
print(df["tamanho_empresa"].value_counts())

# Dicionário para traduzir os níveis de senioridade
traducao_senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

# Aplica a tradução na coluna 'senioridade'
df['senioridade'] = df['senioridade'].map(traducao_senioridade)

# Verifica a contagem após a tradução
print("\nSenioridade apos traducao:")
print(df["senioridade"].value_counts())

# Dicionário para traduzir os tipos de contrato
traducao_contrato = {
    'FT': 'Tempo Integral',
    'CT': 'Contrato',
    'PT': 'Tempo Parcial',
    'FL': 'Freelancer'
}

# Aplica a tradução na coluna 'contrato'
df['contrato'] = df['contrato'].map(traducao_contrato)

# Verifica a contagem após a tradução
print("\nContrato apos traducao:")
print(df["contrato"].value_counts())

# Dicionário para traduzir os tamanhos de empresa
traducao_tamanho_empresa = {
    'M': 'Medio',
    'L': 'Grande',
    'S': 'Pequeno'
}

# Aplica a tradução
df['tamanho_empresa'] = df['tamanho_empresa'].map(traducao_tamanho_empresa)

# Verifica a contagem
print("\nTamanho da empresa apos traducao:")
print(df["tamanho_empresa"].value_counts())

# Dicionário para traduzir a porcentagem de trabalho remoto
traducao_remoto = {
    0: 'Presencial',
    50: 'Hibrido',
    100: 'Remoto'
}

# Aplica a tradução
df['remoto'] = df['remoto'].map(traducao_remoto)

# Verifica a contagem
print("\nTipo de trabalho remoto apos traducao:")
print(df["remoto"].value_counts())

# Visualiza as primeiras linhas após todas as modificações
print("\nDataFrame apos todas as traducoes:")
print(df.head())

# Mostra estatísticas descritivas das colunas do tipo objeto (categóricas)
print("\nEstatisticas descritivas das colunas categoricas:")
print(df.describe(include='object'))

# Remove as linhas com valores nulos e salva em um novo DataFrame
df_limpo = df.dropna()

# Verifica se ainda existem valores nulos
print("\nValores nulos apos limpeza:")
print(df_limpo.isnull().sum())

# Visualiza as primeiras linhas do DataFrame limpo
print("\nPrimeiras linhas do DataFrame limpo:")
print(df_limpo.head())

# Mostra as informações do DataFrame limpo
print("\nInformacoes do DataFrame limpo:")
df_limpo.info()

# Converte a coluna 'ano' para tipo inteiro sem alterar os valores
df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype("int64"))

# Visualiza as primeiras linhas após a conversão
print("\nDataFrame final com a coluna 'ano' convertida para int:")
print(df_limpo.head())

#Aula 3 continuação da aula 1

# Garante que df_limpo ainda tem as colunas com os nomes corretos e os dados traduzidos
df_limpo = df.dropna()

# Gráfico: Quantidade de cargos por nível de experiência
plt.figure(figsize=(6, 4))
df_limpo['nivel_experiencia'].value_counts().plot(kind='bar', title='Quantidade de cargos por nível de experiência')
plt.xlabel('Nível de Experiência')
plt.ylabel('Quantidade')
plt.show()

# Gráfico de barras com salário médio por nível de experiência
ordem = df_limpo.groupby('nivel_experiencia')['salario_em_usd'].mean().sort_values().index

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='nivel_experiencia', y='salario_em_usd', order=ordem)
plt.title('Salário médio por nível de experiência')
plt.xlabel('Nível de experiência')
plt.ylabel('Salário médio anual em USD')
plt.show()

# Histograma dos salários
plt.figure(figsize=(8, 4))
sns.histplot(df_limpo['salario_em_usd'], bins=50, kde=True)
plt.title('Distribuição dos salários anuais')
plt.xlabel('Salário em USD')
plt.ylabel('Frequência')
plt.show()

# Boxplot geral
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['salario_em_usd'])
plt.title('Boxplot dos salários anuais')
plt.xlabel('Salário em USD')
plt.show()

# Boxplot por nível de experiência com ordem correta
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='nivel_experiencia', y='salario_em_usd', data=df_limpo, order=ordem_senioridade)
plt.title('Boxplot dos salários por nível de experiência')
plt.xlabel('Nivel de experiência')
plt.ylabel('Salário em USD')
plt.show()

# Gráfico de pizza do tipo de trabalho
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Distribuição do tipo de trabalho',
             hole=0.5)
fig.update_traces(textinfo='percent+label')
fig.show()

# Mapeamento de regiões
regiao_mapping = {
    'US': 'America do Norte',
    'CA': 'America do Norte',
    'GB': 'Europa',
    'DE': 'Europa',
    'FR': 'Europa',
    'AU': 'Oceania',
    'IN': 'Asia'
}
df_limpo['regiao'] = df_limpo['empresa'].map(regiao_mapping)

# Verifica os dados mapeados
print(df_limpo['regiao'].value_counts())

# Gráfico de barras com salário médio por nível de experiência e região
salario_medio_por_experiencia_regiao = df_limpo.groupby(['nivel_experiencia', 'regiao'])['salario_em_usd'].mean().reset_index()

fig = px.bar(
    salario_medio_por_experiencia_regiao,
    x='nivel_experiencia',
    y='salario_em_usd',
    color='regiao',
    title='Média Salarial por Nível de Experiência e Região',
    labels={
        'nivel_experiencia': 'Nível de Experiência',
        'salario_em_usd': 'Média Salarial Anual (USD)',
        'regiao': 'Região'
    },
    category_orders={'nivel_experiencia': ordem_senioridade}
)
fig.show()
