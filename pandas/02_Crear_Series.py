import pandas as pd

colores = {
    "rojo" : 100,
    "verde" : 200,
    "azul" : 300,
    "negro" : 400
}

var = pd.Series(colores)
print(var)
print(var["rojo"])
print(var["verde"])
print(var["azul"])
print(var["negro"])
# print(var["blanco"])