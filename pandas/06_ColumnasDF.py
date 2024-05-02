import pandas as pd
import numpy as np

# Definimos los datos que van a componer el dataframe
usuarios = {
    "username" : ["victor", "joseph", "gabriel"],
    "email" : ["victor@example.com", "joseph@example.com", "gabriel@example.com"],
    "age" : [34, 35, 36],
    "status" : [True, True, True]
}

# Creamos el dataframe
df = pd.DataFrame(usuarios)
print(df)

# Columnas = Series
# Creamos una nueva serie
calificaciones = pd.Series(np.random.randint(5, 10, 3), index=[0, 1, 2])
print(calificaciones)

# Agregamos la serie al dataframe
df["calificaciones"] = calificaciones
print(df)

# Renombrar las columnas (volver a asignar el dataframe)
df = df.rename(columns={"calificaciones" : "score"})
print(df)

# Eliminar columnas
del df["score"]
print(df)