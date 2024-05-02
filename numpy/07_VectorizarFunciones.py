import numpy as np

# Crear un arreglo de forma tradicional
var = np.random.randint(0,10,20)
print(var)

# Creamos una función y la probamos
def operation(value):
    return (value ** 2) + 2

result = operation(3)
print(result)

# Iteramos sobre el arreglo para ejecutar la función en cada uno de sus elementos
# for value in var:
#     result = operation(value)
#     print(result)
    
# Vectorizamos el arreglo para aplicar sobre cada uno de sus elementos la función deseada
vector = np.vectorize(operation)
var_vectorized = vector(var)
print(var_vectorized)

vector = np.vectorize(lambda value: (value ** 2) + 2)
var_vectorized = vector(var)
print(var_vectorized)