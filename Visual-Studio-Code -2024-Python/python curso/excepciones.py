# excepciones

#print(5 + "3")  #<-- hacer esto es terrorismo

try:
   print("test")
except NameError as error:
   print("error de tipo NameError")
   print(error)
except TypeError:
   print("error de tipo TypeError")
else:       #else solo funciona cuando funciona try
   print("Hola mundo")
finally:
   print("Subscribite")