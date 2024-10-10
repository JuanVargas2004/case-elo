import pandas as pd

funcionarios = pd.read_excel(r"exercicio2/funcionarios.xlsx")
departamento = pd.read_excel(r"exercicio2/departamentos.xlsx")

# print(funcionarios)

df = pd.merge(funcionarios, departamento, left_on="Worker ID", right_on="Worker Ref ID")

df = df.groupby(by="Worker Title")["Salary"].sum()

df = df.sort_values(ascending=False)

print(df.iloc[:2])