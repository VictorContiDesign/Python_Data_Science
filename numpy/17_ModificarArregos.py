import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
a = np.random.randint(0,100,10)
print(a)
print(a.size)

b = np.insert(a, 0, 200)
print(b)
print(b.size)

c = np.append(a, 200)
print(c)
print(c.size)

d = np.delete(c, -1)
print(d)
print(d.size)

e = np.resize(a, 5)
print(e)
print(e.size)

f = np.array([10, 20, 30, 40, 50])
g = np.concatenate([a, f])
print(a)
print(f)
print(g)