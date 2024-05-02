import numpy as np

# Crear un arreglo de forma tradicional
var_1 = np.array([1,2,3,4,5])
print(var_1)

# Crear un arreglo en forma de rango
var_2 = np.arange(0,100)
print(var_2)

# Crear un arreglo en forma de rango con paso
var_3 = np.arange(0,100,2)
print(var_3)

# Crear un arreglo de ceros de tipo flotante
var_4 = np.zeros(10)
print(var_4)

# Crear un arreglo de ceros de tipo entero
var_5 = np.zeros(10, dtype=int)
print(var_5)

# Crear un arreglo de unos de tipo entero
var_6 = np.ones(10, dtype=int)
print(var_6)

# Crear un arreglo a partir de datos basura
# Sirve para crear un arreglo vacio y reservar
# Un espacio en memoria para datos que le introduciremos despues.
var_7 = np.empty(10, dtype=int)
print(var_7)

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
var_8 = np.random.randint(0,100,50)
print(var_8)