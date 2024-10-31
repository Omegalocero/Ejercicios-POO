"""
Ejercicio 5: Desarrollar una función que capitalice palabras en una cadena.
"""

def capitalizar_palabras(cadena):
    return cadena.title()

texto = "buenos dias gente bonita, como andan??"
resultado = capitalizar_palabras(texto)
print(resultado)
