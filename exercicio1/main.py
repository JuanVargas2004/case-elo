import pandas as pd

# Carrega o arquivo Excel contendo os usuários
df = pd.read_excel(r"exercicio1/usuarios.xlsx")

# Obtém o conjunto de IDs de usuários únicos
usuarios_unicos = df["user_id"].unique()

# Itera sobre cada usuário único
for user in usuarios_unicos:
    # Filtra o DataFrame para o usuário atual e ordena as entradas pela data
    user_data = df[df["user_id"] == user].sort_values("date").reset_index(drop=True)
    
    # Verifica se o número de registros do usuário é suficiente para a análise
    if len(user_data) >= 3:
        # Calcula as diferenças entre datas consecutivas
        datas = user_data["date"]
        diferencas = datas.diff().dt.days
        
        # Verifica se há três datas consecutivas (diferença de 1 dia entre elas)
        tres_consecutivos = (diferencas == 1).rolling(window=3).sum() == 2
        
        if tres_consecutivos.any():
            print(f"Usuário com três datas consecutivas encontrado: {user}")
            
            print(diferencas)
            print(  (diferencas == 1).rolling(2).sum() == 2)
            # print(tres_consecutivos)
            
            