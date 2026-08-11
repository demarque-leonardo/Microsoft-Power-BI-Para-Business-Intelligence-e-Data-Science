import pandas as pd

# Importando o set de dados de um arquivo excel
df = pd.read_excel(r"C:\Users\Leonardo Demarque R\Documents\GitHub\Microsoft-Power-BI-Para-Business-Intelligence-e-Data-Science\8_Power_Bi_Para_Analise_de_Dados_Financeiros\database\cru\DadosFinanceiros.xlsx")

# Identificando o schema da database
print(df)

colunas_fixas = ["Tipo", "Componente"]