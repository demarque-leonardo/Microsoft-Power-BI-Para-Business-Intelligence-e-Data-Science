import pandas as pd

# Importando o set de dados de um arquivo excel
df = pd.read_excel(r"8-Power Bi Para Analise de Dados Financeiros\database\DadosFinanceiros.xlsx")

# Identificando o schema da database
print(df)

colunas_fixas = ["Tipo", "Componente"]