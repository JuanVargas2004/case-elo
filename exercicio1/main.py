import pandas as pd

df = pd.read_excel(r"exercicio1/usuarios.xlsx")

usuarios = set(df["user_id"])

for usuario in usuarios:
    
    sub_df = df[df["user_id"] == usuario]
    sub_df = sub_df.sort_values(by="date").reset_index(drop=True)
    
    if len(sub_df) < 3:
        continue
    
    for index in range(len(sub_df) - 2):
        
        data1 = sub_df["date"][index]
        data2 = sub_df["date"][index + 1]
        data3 = sub_df["date"][index + 2]
        
        dif1 = (data2 - data1).days
        dif2 = (data3 - data2).days
        
        if (dif1 == 1) and (dif2 == 1):
            print(f"Usuário encontrado: {usuario}")
