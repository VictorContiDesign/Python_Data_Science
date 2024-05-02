import numpy as np

# Creamos una matriz de 3x5
A = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500],
])
print(A)
print(A.shape)

# Transposición de la matriz
AT = A.T
print(AT)
print(AT.shape)

# Suma total de un subconjunto mediante transposición(columna 4)
print(AT[4].sum())