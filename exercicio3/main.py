import pandas as pd

df = pd.read_excel(r"exercicio3/retencao.xlsx")

df_dezembro = df[df["date"] < "2023-01-01"]
df_janeiro = df[(df["date"] >= "2023-01-01") & (df["date"] < "2023-02-01")]


df_dezembro = df_dezembro.groupby(by="account_id")["user_id"].nunique()
df_janeiro = df_janeiro.groupby(by="account_id")["user_id"].nunique()


series = (df_dezembro / df_janeiro * 100).dropna()

print(series)