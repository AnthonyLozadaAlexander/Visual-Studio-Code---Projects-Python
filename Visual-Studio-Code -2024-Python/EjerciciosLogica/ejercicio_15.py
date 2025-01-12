#Calcular la diferencia en dias de dos fechas dadas.

#importar libreria
from datetime import date

#fecha
hoy = date(2019, 9, 16)
#otra_fecha
otra_fecha = date(2023, 2, 13)

#la diferencia entre las dos fechas
delta = otra_fecha - hoy

#imprimir el contenido de las variables
print(delta)
print(delta.days)