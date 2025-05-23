import os
import pandas as pd

folder = 'f1_data'

# Lista os arquivos CSV
csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]

for csv_file in csv_files:
    path = os.path.join(folder, csv_file)
    df = pd.read_csv(path)
    print(f"Tabela: {csv_file[:-4]}")  # nome do arquivo sem .csv
    print("Colunas:", list(df.columns))
    print("-" * 40)
