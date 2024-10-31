"""
Ejercicio 7: Desarrollar una función “ordenar” que recibe un string y un número (1 o -1). 
Se debe retornar el string ordenado de manera ascendente (si recibió 1 por
parámetros) o descendente (si recibió -1)
Nota: Determinar parámetros y retornos de manera que las funciones sean
genéricas y reutilizables.
"""
def ordenar_cadena(cadena, orden):
    return ''.join(sorted(cadena, reverse=(orden == -1)))

texto1 = "python"
texto2 = "programacion"
texto3 = "hola mundo"

#ascendente
print(f'Cadena original: "{texto1}" -> Orden ascendente: "{ordenar_cadena(texto1, 1)}"')
#descendente
print(f'Cadena original: "{texto2}" -> Orden descendente: "{ordenar_cadena(texto2, -1)}"')
#ascendente
print(f'Cadena original: "{texto3}" -> Orden ascendente: "{ordenar_cadena(texto3, 1)}"')

