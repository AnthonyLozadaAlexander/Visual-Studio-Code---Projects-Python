# Ciclo Anidado De Operadores Logicos
#* Imprimir el numero mayor de los 3 mayores introducidos por el usuario.

numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el segundo numero:"))
numero3 = int(input("Ingrese el tercer numero:"))

if numero1 > numero2 and numero1 > numero3:
  print("El numero mayor es el primero")
else:
  if numero2 > numero1 and numero2 > numero3:
    print("El numero mayor es el segundo")
  else:
    if numero3 > numero1 and numero3 > numero2:
      print("El numero mayor es el tercero")