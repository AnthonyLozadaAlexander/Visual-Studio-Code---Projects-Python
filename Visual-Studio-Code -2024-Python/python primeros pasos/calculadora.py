"""
(1) suma
(2) resta
(3) multi
(4) divis
"""
def calculadora(num1, num2, op):
    print("Bienvenido a la calculadora en python".center(50, "-"))
    if op == 1:
        print(f"El resultado de la suma de: {num1} y {num2}: {num1 + num2}") 
    elif op == 2:
        print(f"El resultado de la resta de: {num1} y {num2}: {num1 - num2}") 
    elif op == 3:
        print(f"El resultado de la multiplicacion de: {num1} y {num2}: {num1 * num2}") 
    elif op == 4:
        print(f"El resultado de la division de: {num1} y {num2}: {num1 / num2}") 
    else:
        print("te equivocaste en la opcion")

variable1 = float(input("introduzca el primer valor: "))
variable2 = float(input("introduzca el segundo valor: "))

calculadora(variable1,variable2,1)
#calculadora(45,23,1)
#calculadora(45,23,2)
#calculadora(45,23,3)
#calculadora(45,23,4)
