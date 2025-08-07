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


