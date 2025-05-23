import pandas as pd
import sqlite3
import os

db_path = os.path.join(os.getcwd(), 'f1.db')
conn = sqlite3.connect(db_path)  

tables = [
    'circuits', 'constructors', 'constructor_results',
    'constructor_standings', 'drivers', 'driver_standings',
    'lap_times', 'pit_stops', 'qualifying', 'races', 'results',
    'seasons', 'sprint_results', 'status'
]

for table_name in tables:
    try:
        df = pd.read_csv(f'f1_data/{table_name}.csv')
        df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
        print(f"Tabela '{table_name}' processada com sucesso.")
    except Exception as e:
        print(f"Erro ao processar '{table_name}': {e}")

conn.close()
