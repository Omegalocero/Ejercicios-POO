"""
Ejercicio 4: Desarrollar una función que convierta los elementos de lista_peli en una
cadena y muestre:
ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
"""

lista_peli = [
    ["Matrix", "El Padrino", "Titanic"],
    ["Forrest Gump", "Pulp Fiction", "Gladiador"],
    ["Blade Runner", "El Rey León", "Volver al Futuro"],
    ["La La Land", "El Gran Lebowski", "Blade Runner"],
    ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
    ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
    ["Titanic", "Star Wars", "El Señor de los Anillos"],
    ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
    ["Forrest Gump", "The Godfather", "Goodfellas"],
    ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]

def convertir_lista_a_cadena(lista):
    for sublista in lista:
        
        if len(sublista) > 1:
            cadena = f'Se recomienda ver "{'", "'.join(sublista[:-1])}" y "{sublista[-1]}"'
        else:
            cadena = f'Se recomienda ver "{sublista[0]}"'
        print(cadena)

convertir_lista_a_cadena(lista_peli)

