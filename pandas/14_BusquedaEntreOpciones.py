import pandas as pd

file = pd.read_csv("users.csv", index_col="id")

# Eliminamos todoas las filas que carezcan de algun valor
file = file.dropna()

# Obtener el nombre de todos los usuarios mayores a 30 anios de los paises
# Canada, Alemania y Francia.
subfile = file[(file["edad"] > 30) & ((file["pais"] == "Canada") | (file["pais"] == "Germany") | (file["pais"] == "France"))]
print(subfile)

subfile = file[(file["edad"] > 30) & (file["pais"].isin(["Canada", "France", "Germany"]))]
print(subfile)