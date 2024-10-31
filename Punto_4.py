"""
4- Herencia de clases
Crear una clase Animal que tenga la característica nombre. 
La clase Perro que herede de Animal las características y realice el sonido “guau guau”. 
La clase Gato que herede de Animal las características y realice el sonido “Miau”. 
Del gato y el perro se debe poder mostrar el sonido que realizan. Se debe crear la clase e implementarla.
"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def sonido(self):
        print(f"{self.nombre} dice: guau guau")

class Gato(Animal):
    def sonido(self):
        print(f"{self.nombre} dice: miau")


mi_perro = Perro("Fabio")
mi_gato = Gato("Mini michi")




