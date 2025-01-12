# Crear una funcion para evaluar un numero y realizar una operacion.

# fn(n): si n <= 15 => 15 - n; (15 - n) * 2

def diferencial(n):
    """
    Calcula la diferencia del valor pasado como argumento.
    Se deben seguir dos reglas.
    
    Si n es menor igual a 15, retornar 15 menos n
    Si no (15 - n) por 2
    """
    if n <= 15:
      return 15 - n
    else:
      return (15 - n) * 2
    
print(diferencial(17))
print(diferencial(3))