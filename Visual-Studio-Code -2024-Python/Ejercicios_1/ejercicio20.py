# Crear un ciclo if,else para saber si un estudiante aprobo o no, la materia.

calificacion1 = int(input("Ingrese la primer calificacion:"))
calificacion2 = int(input("Ingrese la segunda calificacion:"))

#* si la calificacion1 es mayor que 5 Y si la calificacion2 es menor o igual a 10 
#? <= tambien es el limite/rango de dato numerico que el usuario va ingresar por teclado, 
#? si es mayor de ese limite/rango se ejecutara else

print("")

if calificacion1 > 5 & calificacion2 <= 10:
  print("Aprobaste el curso")
  
else:
  print("No aprobaste el curso")