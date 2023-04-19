"""
3. (3 ptos) Crear un programa usando decoradores para medir el
tiempo de ejecución.
- Crear la función decorador adecuadamente que sumará los elementos de la función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo, multiplicación de 4 números para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar (*, **) y visualizar los resultados con un mínimo tres ejemplos.
"""

import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        total = fin - inicio
        print("La función multiplicar tardó {} segundos en ejecutarse" .format(total))
        return resultado
    return wrapper

@medir_tiempo
def multiplicar(a,b,c,d):
    resultado = a*b*c*d
    return resultado

print(multiplicar(2, 3, 4,2))
print(multiplicar(5, 10,5,6))
print(multiplicar(3, 6, 9, 0))
