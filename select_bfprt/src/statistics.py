import pandas as pd

file_name = '60000_10000.csv'
dataset_path = f'data/{file_name}'

columns = ['uuid', 'worker_id', 'dataset_name', 'algorithm_name', 'n', 'k', 'output', 'execution_time', 'error']
df = pd.read_csv(dataset_path, names=columns)

# Calculando a média e o desvio padrão agrupados por nomes de algoritmos
df_grouped = df.groupby('algorithm_name')['execution_time'].agg(['mean', 'std']).reset_index()

# Renomeando as colunas
df_grouped.columns = ['Algoritmo', 'Tempo Médio de Execução', 'Desvio Padrão']

# Mostrando a tabela
print(df_grouped)
