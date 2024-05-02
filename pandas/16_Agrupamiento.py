import pandas as pd

file = pd.read_csv("users.csv", index_col="id")

# Eliminamos todoas las filas que carezcan de algun valor
file = file.dropna()

# Mostrar en consola la cantidad de hombres y mujeres del dataset
group = file.groupby("genero")["genero"].count()
print(group)

# Mostrar el pais con mas mujeres
country_more_females = file[file["genero"] == "female"].groupby("pais")["pais"].count().sort_values().tail(1)
print(country_more_females)