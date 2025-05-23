import pandas as pd
import sqlite3
import os

conn = sqlite3.connect('f1.db')

tables = [
    'circuits', 'constructors', 'constructor_results',
    'constructor_standings', 'drivers', 'driver_standings',
    'lap_times', 'pit_stops', 'qualifying', 'races', 'results',
    'seasons', 'sprint_results', 'status'
]

for table in tables:
    file_path = f'f1_data/{table}.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f'Inserindo dados na tabela {table}...')
        df.to_sql(table, conn, if_exists='append', index=False)
    else:
        print(f'Arquivo {file_path} não encontrado, pulando.')

conn.commit()
conn.close()
print("Dados inseridos com sucesso!")
