import pandas as pd

file = pd.read_csv("users.csv", index_col="id")

# Eliminamos todoas las filas que carezcan de algun valor
file = file.dropna()

# Obtener todos los usuarios entre las edades 40 y 50
subfile = file[(file["edad"] >= 40) & (file["edad"] <= 50)]
print(subfile)

subfile = file[file["edad"].between(40, 50)]
print(subfile)