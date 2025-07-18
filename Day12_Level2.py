#NIVEL 2

import random
import string
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

def list_of_hexa_colors(num_colores=1):

    colores_hex = []
    caracteres_hex = '0123456789abcdef'
    for _ in range(num_colores):
        color = '#' + ''.join(random.choices(caracteres_hex, k=6))
        colores_hex.append(color)
    return colores_hex

# Ejemplo de uso:
print("Lista de 5 colores hexadecimales:")
print(list_of_hexa_colors(5))
print("-" * 20)


def list_of_rgb_colors(num_colores=1):

    colores_rgb = []
    for _ in range(num_colores):
        # Reutilizamos la función del Nivel 1
        colores_rgb.append(rgb_color_gen()) 
    return colores_rgb

# Ejemplo de uso:
print("Lista de 3 colores RGB:")
print(list_of_rgb_colors(3))
print("-" * 20)


def generate_colors(tipo, cantidad):

    if tipo.lower() == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo.lower() == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo de color no válido. Elige 'hexa' o 'rgb'."

# Ejemplos de uso:
print("Generar 3 colores hexa:")
print(generate_colors('hexa', 3))

print("\nGenerar 2 colores rgb:")
print(generate_colors('rgb', 2))
print("-" * 20)