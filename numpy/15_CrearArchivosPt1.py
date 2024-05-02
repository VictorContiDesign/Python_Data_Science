import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
a = np.random.randint(0,100,10)
print(a)

np.savetxt("arreglo.txt", a, fmt="%i")

b = np.loadtxt("arreglo.txt")
print(b.dtype)

c = np.loadtxt("arreglo.txt", dtype=int)
print(c.dtype)

print(a.size)
d = a.reshape((2,5))
print(d)

np.savetxt("matriz.csv", d, fmt="%i", delimiter=",")
e = np.loadtxt("matriz.csv", delimiter=",", dtype=int)
print(e)
print(e.dtype)