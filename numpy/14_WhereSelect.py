import numpy as np

# Crear un arreglo a partir de números enteros aleatorios
# Argumentos: Principio, Final, Cantidad de elementos
calificaciones = np.random.randint(1,11,10)
print(calificaciones)
print(type(calificaciones))

# Todas las calificaciones mayores o igual a 7 son aprobatorias
result_1 = np.where(calificaciones >= 7, "Felicidades, aprobaste la materia", "Lo sentimos, no aprobaste la materia")
print(result_1)

# 4 Tipos de mensajes
condiciones = [
    (calificaciones == 10),
    ((calificaciones == 8) | (calificaciones == 9)),
    (calificaciones == 7),
    (calificaciones < 7),
]

opciones = [
    "Felicidades, aprobaste la materia con 10",
    "Felicidades, aprobaste la materia",
    "Aprobaste la materia",
    "Lo sentimos, no aprobaste la materia"
]

result_2 = np.select(condiciones, opciones)
print(result_2)

calificaciones = np.append(calificaciones, 7)
print(calificaciones)

#Volvemos a construir las condiciones ya que hemos modificado las calificaciones
condiciones = [
    (calificaciones == 10),
    ((calificaciones == 8) | (calificaciones == 9)),
    (calificaciones == 7),
    (calificaciones < 7),
]

result_3 = np.select(condiciones, opciones)
print(result_3)