import pandas as pd

file = pd.read_csv("users.csv", index_col="id")
print(file)

# loc (indices tipo string)
# iloc (indices tipo entero)

print(file.iloc[0])
print(file.iloc[199])

# Generamos un subdataframe con las primeras 5 filas del dataframe originar
subfile = file.iloc[0:5]
print(subfile)
subfile = file.iloc[:5]
print(subfile)

#######################
# BUSQUEDA POR INDICE #
#######################

# Definir que valores de columnqs queremos obtener en un sub-dataframe
# Con este formato los indices de las columnas deben ser numéricos también
subfile = file.iloc[:3,[0, 2, 4]]
print(subfile)
# Con este formato los indices de las columnas pueden ser los nombres de las columnas
subfile = file.iloc[:3][["nombre", "genero", "email"]]
print(subfile)