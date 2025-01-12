# En una "lista" de numeros, retorna el segundo numero mas grande.
#
# Ejemplo: [5,7,2,7,9,4,8]
# Respuesta: 8

lista = [5,7,2,7,9,4,8,11]
lista.sort()
print(lista[-2])



# Conversor Tiempo
# Crea una funcion que reciba dias , horas, minutos y segundos
# (como "list") y retorne su resultado en milisegundos.

def militime(day = 0, hour = 0, minute = 0, second = 0):
     final_time = 0
     hour =+ day * 24
     minuto = hour * 60
     second = minute * 60
     final_time = second * 1000
     print(final_time)

militime(2,33,24,12)

# Fizzbuz
# Escribe una funcion que imprima los numeros del 1 al 100 
# con un salto de linea entre cada uno, sustituyendo los siguientes
# Multiplos de tres por la palabra "Fizz"
# Multiplos de cinco por la palabra "Buzz"
# Multiplo de tres y cinco a la vez por la palabra "fizzbuzz"

def fizzbuzz():
     for a in range(1, 101):
          if a % 3 == 0 and a % 5 == 0:
               print("fizzbuzz")
          elif a % 3 == 0:
               print("fizz")
          elif a % 5 == 0:
              print("buzz")
          else:
               print(a)

fizzbuzz()
               