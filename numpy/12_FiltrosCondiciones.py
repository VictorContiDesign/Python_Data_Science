import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
a = np.random.randint(0,100,50)
print(a)

# Operadores Condicionales
print(a > 50)

# Creamos un segundo arreglo
b = np.array([1, 2, 3, 4, 5])
print(b)

# Obtener elementos mediante máscaras
print(b[[True, False, False, False, True]])

# Obtener un subconjunto que cumpla una condición
print(a[a > 50])

# Operadores lógicos
print(a[(a > 50) & (a < 90)])
print(a[(a == 10) | (a == 20) | (a == 50)])