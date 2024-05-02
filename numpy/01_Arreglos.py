import numpy as np

# Los arreglos tienen que ser del mismo tipo
var = np.array([1,2,3,4,5])
# Retornar el array
print(var)
# Retornar el tipo del array
print(type(var))
# Retornar el tamaño del array
print(var.size)
# Retornar la dimension del array
print(var.ndim)
# Rertorna el tipo de datos que usa el arreglo
print(var.dtype)
# Retorna las dimensiones del array como la cantidad de elementos que hay en ellas
print(var.shape)