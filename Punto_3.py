"""
3- Clase para representar una Calculadora Crear una clase Calculadora que pueda calcular
suma, resta, multiplicación y división.
Se debe crear la clase e implementarla.
"""

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b if b != 0 else "Error: División por cero"

calculadora = Calculadora()

A = int(input("Escriba el primer valor del numero para la operacion: "))

operacion = input("Que tipo de operacion desea realizar? (+, -, *, o /): ")


while operacion != "+" and operacion != "-" and operacion != "*" and operacion != "/":
    operacion = input("Operación inválida. Por favor ingrese nuevamente una operación válida (+, -, *, o /): ")

B = int(input("Escriba el segundo valor del numero para la operacion: "))

if operacion == "+":
    resultado = calculadora.suma(A, B)
elif operacion == "-":
    resultado = calculadora.resta(A, B)
elif operacion == "*":
    resultado = calculadora.multiplicacion(A, B)
elif operacion == "/":
    resultado = calculadora.division(A, B)


print(f"El resultado de {A} {operacion} {B} es: {resultado}")
