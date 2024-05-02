import pandas as pd

usuarios = {
    "username" : ["victor", "joseph", "gabriel"],
    "email" : ["victor@example.com", "joseph@example.com", "gabriel@example.com"],
    "age" : [34, 35, 36],
    "status" : [True, True, True]
}

df = pd.DataFrame(usuarios)
print(df["username"])
print(df.username)
print(df.email)
print(df.age)
print(df.status)
print(df["age"][1])
print(df.columns)
print(df.values)