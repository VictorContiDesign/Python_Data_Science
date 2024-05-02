import pandas as pd
import numpy as np

# Python : None
# Numpy o Pandas : NaN

var_1 = pd.Series([1, 2, 3, np.nan, np.nan, np.nan, 6, 7, 8])
print(var_1)

# isnull - notnull
print(var_1.isnull())
print(var_1.notnull())

var_2 = var_1[var_1.isnull()]
print(var_2)

var_3 = var_1[var_1.notnull()]
print(var_3)