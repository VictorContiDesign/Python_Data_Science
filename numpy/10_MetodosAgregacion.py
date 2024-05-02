import numpy as np

# Creamos una matriz de 3x5
A = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500],
])
print(A)

# Desviación estándar del arreglo
print(A.std())

# Suma de todos los elementos del arreglo
print(A.sum())

# Valor mínimo del arreglo
print(A.min())

# Valor máximo del arreglo
print(A.max())

# Valor promedio del arreglo
print(A.mean())

# Suma de un subconjunto del arreglo (fila 1)
print(A[1].sum())

# Mínimo de un subconjunto del arreglo (fila 1)
print(A[1].min())

# Máximo de un subconjunto del arreglo (fila 1)
print(A[1].max())

# Promedio de un subconjunto del arreglo (columna 2)
print(A[:, 2].mean())