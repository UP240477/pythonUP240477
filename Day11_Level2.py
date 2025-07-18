
#NIVEL 2

import statistics
from collections import Counter

# Función que cuenta pares e impares hasta un número dado
def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"El número de impares es {odds}.")
    print(f"El número de pares es {evens}.")

# Función que calcula el factorial de un número
def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Entrada no válida. El número debe ser un entero no negativo."
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Función que comprueba si un parámetro está vacío
def is_empty(param):
    return not param

# Funciones de estadística para una lista de números
def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    try:
        return statistics.mode(lst)
    except statistics.StatisticsError:
        return "No hay una única moda."

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)