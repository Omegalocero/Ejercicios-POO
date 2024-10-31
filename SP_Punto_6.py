"""
Ejercicio 6: Desarrollar una función que verifique si una cadena es un palíndromo:
Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta
la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo,
anilina.
"""

def es_palindromo(cadena):
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    return cadena == cadena[::-1]

texto1 = "Anilina"
texto2 = "Hola Bonna Tarda"
texto3 = "i want to break free"

print(f'¿"{texto1}" es un palindromo? {es_palindromo(texto1)}')  # True
print(f'¿"{texto2}" es un palindromo? {es_palindromo(texto2)}')  # False
print(f'¿"{texto3}" es un palindromo? {es_palindromo(texto3)}')  # True

