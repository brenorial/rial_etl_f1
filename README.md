# Projeto ETL Fórmula 1

Este projeto tem como objetivo extrair, transformar e carregar (ETL) dados públicos da Fórmula 1 para um banco de dados SQLite, além de gerar diagramas ER das tabelas com seus relacionamentos.

---

## Estrutura do projeto

```

rial\_formula\_1/
├── f1\_data/               # Arquivos CSV com dados brutos
│   ├── circuits.csv
│   ├── constructors.csv
│   ├── drivers.csv
│   ├── races.csv
│   └── ... (demais tabelas)
├── extract.py             # Script principal para ETL (criação e inserção no DB)
├── colunas.py             # Script para mostrar colunas das tabelas (diagnóstico)
├── f1.db                  # Banco de dados SQLite gerado (após execução)
├── er\_diagram.png         # Diagrama ER gerado pelo ERAlchemy
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo de documentação

```

---

## Objetivo

- Carregar os dados CSV originais para um banco de dados relacional SQLite.
- Definir chaves primárias (PK) e estrangeiras (FK) para garantir integridade referencial.
- Permitir consultas eficientes no banco SQLite.
- Gerar diagramas ER (Entidade-Relacionamento) com tabelas e relacionamentos para análise visual da estrutura dos dados.

---

## Tecnologias usadas

- Python 3.12+
- Pandas (para manipulação de CSV e inserção no DB)
- SQLite (banco de dados relacional leve)
- ERAlchemy (para gerar diagramas ER)
- Graphviz (para renderizar imagens do diagrama ER)

---

## Passo a passo para rodar o projeto

### 1. Preparar ambiente Python

Recomenda-se criar um ambiente virtual e instalar dependências:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows PowerShell

pip install --upgrade pip
pip install pandas sqlalchemy eralchemy graphviz
```

---

### 2. Preparar banco SQLite

O script `extract.py` cuida da criação das tabelas com suas chaves primárias e estrangeiras, além de importar os dados dos CSVs para o banco.

Execute:

```bash
python extract.py
```

Se já existir o arquivo `f1.db`, ele pode ser substituído para garantir tabela atualizada.

---

### 3. Gerar diagrama ER

Após criar o banco, gere o diagrama ER para visualizar tabelas e relacionamentos:

```bash
eralchemy -i sqlite:///f1.db -o er_diagram.png
```

Ou, via Python:

```python
from eralchemy import render_er

render_er('sqlite:///f1.db', 'er_diagram.png')
```

Abra o arquivo `er_diagram.png` para ver o esquema visual.

---

## Sobre o banco de dados

### Principais tabelas e suas relações:

- `circuits` - Pistas onde as corridas são realizadas (PK: `circuitId`)
- `races` - Corridas realizadas em cada temporada, referenciando `circuits` (FK: `circuitId`)
- `drivers` - Pilotos (PK: `driverId`)
- `constructors` - Equipes (PK: `constructorId`)
- `results` - Resultados das corridas, referenciando `races`, `drivers` e `constructors`
- ... e outras tabelas para detalhes como tempos de volta, paradas nos boxes, etc.

Todas as tabelas possuem chaves primárias para garantir unicidade, e as chaves estrangeiras estabelecem integridade referencial entre elas.

---

## Estrutura das tabelas

Você pode consultar as colunas e tipos executando o script `colunas.py`, que lista todas as tabelas e seus campos.

---

## Dicas para desenvolvimento

- Garanta que as tabelas estejam criadas com PK e FK antes de inserir dados.
- Para evitar erros, remova o arquivo SQLite antigo (`f1.db`) antes de recriar.
- Instale o Graphviz corretamente para o ERAlchemy gerar diagramas sem problemas.
- Atualize o `requirements.txt` com as versões específicas usadas.
