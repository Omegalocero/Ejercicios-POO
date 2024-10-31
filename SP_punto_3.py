"""
Ejercicio 3: Desarrollar una función que reemplaza una palabra específica por otra
en una cadena
"""


def palabra(cadena, vieja, nueva):
    return cadena.replace(vieja, nueva)


texto = input("Ingrese la cadena de texto: ")

palabra_reemplazada = input("Ingrese la palabra que desea reemplazar: ")

nueva_palabra = input("Ingrese la nueva palabra para reemplazarla: ")

resultado = palabra(texto, palabra_reemplazada, nueva_palabra)

print("Cadena modificada:", resultado)
