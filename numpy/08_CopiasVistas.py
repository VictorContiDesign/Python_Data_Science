import numpy as np

print("###################")
var = np.arange(0,10)
print("var : ", var)
print("id var : ", id(var))
print("###################")

# Una copia es un arreglo creado a partir de otro que contiene los mismos objetos
# Los cambios en el arreglo original no se ven reflejados en las copias
var_copy = var.copy()
var[0] = 100
print("var : ", var)
print("id var : ", id(var))
print("var_copy : ", var_copy)
print("id var_copy : ", id(var_copy))
print("###################")

print(var is var_copy)
print("###################")

# Una vista apunta al arreglo original
# Los cambios en el arreglo original se ven reflejados las vistas
var_view = var.view()
var[0] = 200
print("var : ", var)
print("id var : ", id(var))
print("var_view : ", var_view)
print("id var_view : ", id(var_view))
print("###################")

print(id(var))
print(id(var_view.base))
print("###################")

print(var is var_view.base)
print("###################")

# Otra manera de crear vistas en numpy
var_view = var[:]
print(var is var_view.base)
print("###################")