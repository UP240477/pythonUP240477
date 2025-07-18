import math
from collections import Counter
import countries_data

# Función que suma dos números
def add_two_numbers(a, b):
    return a + b

# Función que calcula el área de un círculo: area = π * r^2
def area_of_circle(r):
    return math.pi * r * r

# Función que suma un número arbitrario de argumentos
def add_all_nums(*args):
    suma = 0
    for num in args:
        if isinstance(num, (int, float)):
            suma += num
        else:
            return "Error: Todos los elementos deben ser números."
    return suma

# Función que convierte grados Celsius a Fahrenheit: °F = (°C * 9/5) + 32
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función que determina la estación del año según el mes
def check_season(month):
    month = month.lower()
    if month in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif month in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif month in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif month in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes no válido'

# Función para calcular la pendiente entre dos puntos (x1, y1) y (x2, y2)
# Pendiente m = (y2 - y1) / (x2 - x1)
def calculate_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x2 - x1 == 0:
        return "La pendiente es indefinida (línea vertical)."
    return (y2 - y1) / (x2 - x1)

# Función que resuelve una ecuación cuadrática: ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    discriminante = (b**2) - (4*a*c)
    if discriminante > 0:
        sol1 = (-b - math.sqrt(discriminante)) / (2*a)
        sol2 = (-b + math.sqrt(discriminante)) / (2*a)
        return {sol1, sol2} # Devuelve un conjunto con dos soluciones
    elif discriminante == 0:
        sol = -b / (2*a)
        return {sol} # Devuelve un conjunto con una solución
    else:
        return "No hay soluciones reales."

# Función que imprime cada elemento de una lista
def print_list(lst):
    for item in lst:
        print(item)

# Función que invierte una lista usando un bucle
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# Función que pone en mayúscula la primera letra de cada elemento de una lista
def capitalize_list_items(lst):
    capitalized_list = []
    for item in lst:
        if isinstance(item, str):
            capitalized_list.append(item.capitalize())
    return capitalized_list

# Función que añade un elemento al final de una lista
def add_item(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list

# Función que elimina un elemento de una lista
def remove_item(lst, item):
    new_list = lst.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list

# Función que suma todos los números en un rango hasta n
def sum_of_numbers(n):
    return sum(range(n + 1))

# Función que suma todos los números impares en un rango
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

# Función que suma todos los números pares en un rango
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

