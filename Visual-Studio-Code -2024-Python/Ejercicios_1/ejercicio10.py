# Ejercicio 9: Mostrar la fecha de un evento almacenada en una tupla

fecha_evento = (2023, 9, 14)

print(type(fecha_evento))

print(fecha_evento)

print("El evento programado sera para la fecha:", fecha_evento)

print("El evento programado sera para la fecha: %i%i%i" % fecha_evento)

anio, mes, dia = fecha_evento

print("El evento programado sera para la fecha: {}/{}/{}".format(anio, mes, dia))