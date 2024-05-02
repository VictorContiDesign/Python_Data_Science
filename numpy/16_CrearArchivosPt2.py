import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
a = np.random.randint(0,100,10)
print(a)

np.save("arreglo_binario.npy", a)

b = np.load("arreglo_binario.npy")
print(b)