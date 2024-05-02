import numpy as np

# Crear un arreglo de forma tradicional
var = np.random.randint(0,10,10)
print(var)

# Búsqueda por índice
elemento = var[2]
print(elemento)

elemento = var[-2]
print(elemento)

# Modificar por índice
var[2] = 100
print(var)