"""
Ejercicio 2: Desarrollar una función que cuente cuántas palabras hay en una cadena.
"""


def contar_palabras(cadena):
    return len(cadena.split())

texto = "m a n z a n a"

resultado = contar_palabras(texto)
print(resultado)
