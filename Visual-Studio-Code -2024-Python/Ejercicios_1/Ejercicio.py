# Pedir la edad al usuario , si es menor de 12 = Kid , Si eres mayor a 18 = Adult , Si eres mayor a 18 y 25 = Adult , Get a Job 

edad = int(input("edad="))

if edad < 12:
  print("Kid")
elif edad < 18:
  print("Adolescent")
  
if edad > 18:
  print("Adult")
  if edad > 25:
    print("Get a Job")

print("End")


   
