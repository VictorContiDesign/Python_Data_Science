import numpy as np

# Crear un arreglo de forma tradicional
var = np.random.randint(0,10,20)
print(var)

# Obtener un rango de elementos dentro del arreglo de forma tradicional
# var[start:end:saltos]
sub_var = var[2:8]
print(sub_var)
sub_var = var[:8]
print(sub_var)
sub_var = var[2:]
print(sub_var)
sub_var = var[2:8:2]
print(sub_var)

# Obtener elementos individuales por índices dentro del arreglo de forma numpy
sub_var = var[[2,4,6]]
print(sub_var)

# Creamos una máscara de booleanos para obtener ciertos elementos de un arreglo
var = np.random.randint(0,10,5)
# La máscara debe poseer la misma cantidad de elementos que el array
print(var)
var_masked = var[[True, False, False, False, True]]
print(var_masked)

