import pandas as pd

file = pd.read_csv("users.csv", index_col="id")
print(file)

print(file.head(10))
print(file.tail(10))
