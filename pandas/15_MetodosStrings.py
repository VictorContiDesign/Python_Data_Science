import pandas as pd

file = pd.read_csv("users.csv", index_col="id")

# Eliminamos todoas las filas que carezcan de algun valor
file = file.dropna()

# startswith - endswith - contains
subfile = file[file["email"].str.startswith("a")]
print(subfile)

subfile = file[file["email"].str.endswith(".com")]
print(subfile)

subfile = file[file["nombre"].str.contains("Gabriel")]
print(subfile)