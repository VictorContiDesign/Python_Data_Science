import numpy as np

# Creamos una matriz de 3x5
A = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500],
])
print(A)

# Dimensiones de la matriz
print(A.ndim)

# Conocer la forma del arreglo
# Filas x Columnas
print(A.shape)

# Acceder a elementos de la matriz
print(A[0][0])
print(A[1][2])
print(A[2][4])
print(A[-1][-1])

# Otra forma de acceder a elementos de la matriz
print(A[0, 0])
print(A[1, 2])
print(A[2, 4])
print(A[-1, -1])

# Acceder a rangos de elementos
print(A[1, :3])
print(A[2, 2:])

# Acceder a múltiples elementos individuales
print(A[0, [0, 4]])

# Acceder a valores de columnas
print(A[:, 3])
print(A[[0, 2], 3])