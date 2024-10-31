"""
2 - Clase para representar un Rectángulo Crear una clase rectángulo que tenga las
características base y altura.
Del rectángulo se debe poder calcular el área y el perímetro.
Se debe crear la clase e implementarla.
"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

base = float(input("Ingrese la base del rectángulo: "))

altura = float(input("Ingrese la altura del rectángulo: "))

rectangulo = Rectangulo(base, altura)

print(f"El area del rectángulo es: {rectangulo.area()}")

print(f"El perimetro del rectángulo es: {rectangulo.perimetro()}")


