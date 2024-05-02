import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
a = np.random.randint(0,10,20)
print(a)
print(a.size)

# arreglo.sort() modifica el arreglo original
a.sort()
print(a)

b = a[::-1]
print(b)

# np.sort() no modifica el arreglo original
c = np.random.randint(0,10,20)
d = np.sort(c)
e = np.sort(d)[::-1]
print(c)
print(d)
print(e)