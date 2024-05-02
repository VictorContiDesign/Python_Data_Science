import pandas as pd

file = pd.read_csv("users.csv", index_col="id")

# Eliminamos todoas las filas que carezcan de algun valor
file = file.dropna()
print(file)

# Obtener el usuario mas joven de Canada
file_age_min_CA = file[file["pais"] == "Canada"].sort_values("edad").head(1)
print(file_age_min_CA)

# Obtener a los 5 usuarios mas jovenes de Alemania
file_age_max_GE = file[file["pais"] == "Germany"].sort_values("edad", ascending=False).head(5)
print(file_age_max_GE)