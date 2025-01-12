# Pedir la edad al usuario , si es menor de 12 = Kid , Si eres mayor a 18 = Adult , Si eres mayor a 18 y 25 = Adult , Get a Job 

edad = int (input("edad ="))

if edad > 18 and edad > 25:
  print("Adult")
  print("Get a Job")
elif edad > 18:
  print("Adult")
elif edad < 12:
  print("Kid")

print("End")