import pandas as pd

# loc (indices tipo string)
# iloc (indices tipo entero)

# Definimos los datos que van a componer el dataframe
usuarios = {
    "username" : ["victor", "joseph", "gabriel"],
    "email" : ["victor@example.com", "joseph@example.com", "gabriel@example.com"],
    "age" : [34, 35, 36],
    "status" : [True, True, True]
}

# Creamos el dataframe
df = pd.DataFrame(usuarios, index=["a", "b", "c"])
print(df.index)
print(df)

# Accedemos filas por indices string
print(df.loc["a"])
print(df.loc["c"])

# Generamos un subdataframe con las primeras dos filas
subdf = df.loc["a":"b"]
print(subdf)
subdf = df.loc["a":"b", ["username", "email"]]
print(subdf)
subdf = df.loc["a":"b"][["username", "email"]]
print(subdf)