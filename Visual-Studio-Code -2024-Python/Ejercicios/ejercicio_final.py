# Codigo Para Calcular El Indice De Masa Corporal

Peso = float(input("Introduzca el Peso: "))
Altura = float(input("Introduzca la Altura: "))

IMC = Peso / (Altura ** 2)

if (IMC < 18.5):
  print("Insuficiencia Ponderal (Bajo Peso)")
  
elif(IMC > 18.5 and IMC < 24.9):
  print("Intervalo Normal")
  
elif(IMC >= 25 and IMC < 29.9):
  print("Sobrepeso")

else:
  print("Obesidad")
  
print(IMC)