
#NIVEL 3

import random

def shuffle_list(lista_original):

    lista_copiada = lista_original.copy()
    random.shuffle(lista_copiada)
    return lista_copiada

# Ejemplo de uso:
mi_lista = [1, 2, 'a', 'b', True, False]
print(f"Lista original: {mi_lista}")
print(f"Lista mezclada: {shuffle_list(mi_lista)}")
print(f"La lista original no ha cambiado: {mi_lista}")
print("-" * 20)


def unique_random_numbers():
    """
    Devuelve una lista de 7 números aleatorios únicos en el rango de 0 a 9.
    """
    numeros = random.sample(range(10), 7)
    return numeros

# Ejemplo de uso:
print("Siete números aleatorios y únicos entre 0 y 9:")
print(unique_random_numbers())
print("-" * 20)