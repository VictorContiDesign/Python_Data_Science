import numpy as np

var_1 = np.array([1,2,3,4,5])
print(var_1)
print(var_1.dtype)

var_2 = np.array([1,2,3,4,5], dtype=float)
print(var_2)
print(var_2.dtype)

var_3 = np.array([1,2,3,4,5], dtype=str)
print(var_3)
print(var_3.dtype)

var_4 = np.array([1,2,3,4,5], dtype=bool)
print(var_4)
print(var_4.dtype)

var_5 = np.array([0,2,3,4,5], dtype=bool)
print(var_5)
print(var_5.dtype)

var_6 = np.array([0,2,3,4,5], dtype=complex)
print(var_6)
print(var_6.dtype)