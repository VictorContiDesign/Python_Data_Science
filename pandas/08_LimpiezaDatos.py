import pandas as pd

file = pd.read_csv("users.csv", index_col="id")
print(file)

# Eliminamos toda fila que tenga algun valor vacio
# Se debe reasignar el dataframe
# file = file.dropna()
# print(file)

# Rellenmos con un valor por defecto las celdas vacias
# Se debe reasignar el dataframe
# file = file.fillna("Nuevo valor")
# print(file)
file = file.fillna({"nombre" : "Sin nombre", "email" : "example@example.com"})
print(file)