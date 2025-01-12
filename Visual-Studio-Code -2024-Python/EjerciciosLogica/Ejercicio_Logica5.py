# Ejercicio 4: Solicitar el valor del radio de un circulo para calcular su area.

from math import pi

r = float(input("Escriba el radio del circulo: "))

area = pi * r ** 2

print("El area del circulo es {}".format(area))