import pandas as pd

usuarios = {
    "username" : ["victor", "joseph", "gabriel"],
    "email" : ["victor@example.com", "joseph@example.com", "gabriel@example.com"],
    "age" : [34, 35, 36],
    "status" : [True, True, True]
}

df = pd.DataFrame(usuarios)
print(df)

df = pd.DataFrame(usuarios, index=["a", "b", "c"])
print(df)