import pandas as pd

file = pd.read_csv("users.csv", index_col="id")
print(file)

# Eliminamos todoas las filas que carezcan de algun valor
file = file.dropna()
print(file)

# Obtener el nombre de todos los usuarios del pais Canada
condition_1 = (file["pais"] == "Canada")
print(condition_1)

result_1 = file[file["pais"] == "Canada"]
print(result_1)
result_1_name = file[file["pais"] == "Canada"]["nombre"]
print(result_1_name)

# Obtener el nombre y correo electronico de todos los usuarios con edad mayor a 50
condition_2 = (file["edad"] > 50)
print(condition_2)

result_2_name_age = file[file["edad"] > 50][["nombre", "edad"]]
print(result_2_name_age)

# Obtener el promedio de todos los usuarios de sexo femenino con una edad mayor a 30
condition_3 = (file["genero"] == "female")
print(condition_3)
condition_4 = (file["edad"] > 30)
print(condition_4)
condition_5 = ((file["genero"] == "female") & (file["edad"] > 30))
print(condition_5)

result_3_age_female_mean = file[(file["genero"] == "female") & (file["edad"] > 30)]["edad"].mean()
print(result_3_age_female_mean)