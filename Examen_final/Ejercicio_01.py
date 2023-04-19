"""
1. Escribir un programa para el manejo de listas el
cuál cumplirá los siguientes
requerimientos (4 ptos):
"""
import random

lista_1 = []

# - Crear una función que le permitirá almacenar 10 número aleatorios en una lista y finalmente los imprimirá por consola al llamar la función.
def almacenar_numeros(lista):
    for i in range(10):
        lista.append(random.randint(1, 20))
    return lista

print("La lista principal es {}" .format(almacenar_numeros(lista_1)))

# - Crear una función que le permita almacenar los números no repetidos de la lista anterior, retornar este valor e imprimirlo por consola.
def almacenar_no_repetidos(lista):
    lista_sin_repetidos = []
    for num in lista:
        if lista.count(num) == 1:
            lista_sin_repetidos.append(num)
    return lista_sin_repetidos

lista_2 = almacenar_no_repetidos(lista_1)
print("La lista con numeros no repetidos es {}".format(lista_2))


# - Crear una función donde se creará una lista para ordenar de mayor a menor
# la lista que se creó en el ítem anterior (número no repetidos) y otra lista
# para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
# consola.

def ordenar(lista):
    lista_a = sorted(lista, reverse=True)
    lista_b = sorted(lista)
    print("La lista de mayor a menor es {}".format(lista_a))
    print("La lista de menor a mayor es {}".format(lista_b))

ordenar(lista_2)


# - Crear una función para indicar cuál es mayor número de la lista (lista del
# ítem 2), retornar este valor e imprimirlo por consola.

def mayor_valor(lista):
    return max(lista)

print("El mayor numero de la lista es {}" .format(mayor_valor(lista_2)))