# Calcular el IMC (Indice De Masa Corporal)

Peso = int(input("Escriba el Peso: "))  #Dato numerico entero
Altura = float(input("Escriba la Altura: "))  #Dato numerico flotante

Resultado = Peso / (Altura ** 2)
print(f"El IMC de es: {Resultado}")