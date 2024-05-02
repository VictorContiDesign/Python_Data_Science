import pandas as pd

########
# Series
# Poseen dos arreglos
# Un arreglo que posee los valores de la serie
# Otro arreglo que posee los índices de la serie

var_1 = pd.Series([1,2,3,4,5])
print(var_1)
print(type(var_1))
print(var_1.size)
print(var_1.dtype)
print(var_1.shape)
print(var_1.index)

var_1[4] = 18
print(var_1)

var_2 = pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e"], name="Numeros")
print(var_2)
var_2["a"] = 10
print(var_2)
var_2 = pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e"], name="Numeros", dtype=int)
print(var_2)
var_2 = pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e"], name="Numeros", dtype=float)
print(var_2)
var_2 = pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e"], name="Numeros", dtype=bool)
print(var_2)
var_2 = pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e"], name="Numeros", dtype=str)
print(var_2)