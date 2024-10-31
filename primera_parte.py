"""
1 -Clase para representar un Libro
Crear una clase Libro que tenga las características título, autor y año de publicación. 
Del libro se debe poder obtener información, mostrando por mensaje todos sus datos. 
Se debe crear la clase e implementarla.
"""
class Libro: 
    def __init__(self, titulo, autor, publicado):
        self.titulo = titulo
        self.autor = autor
        self.publicado = publicado
        

libro_1 = Libro("Las aventuras de Pepito", "Pepito", "13/6/2024")
libro_2 = Libro("Las aventuras de Juan", "Daniel", "22/2/2024")

print(type(libro_1))
print(type(libro_2))

print(libro_1.autor, libro_1.autor, libro_1.publicado)
print(libro_2.titulo, libro_2.autor, libro_2.publicado)
