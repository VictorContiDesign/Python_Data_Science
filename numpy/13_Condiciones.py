import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
a = np.random.randint(0,100,50)
print(a)

# All
print(np.all(a > 50))
print(np.all(a >= 0))
print(np.all(a <= 100))

# Any
print(np.any((a >= 0) & (a <= 100)))
print(np.any(a > 10))
print(np.any(a > 200))