import random
import string

def random_user_id():
    # Define el conjunto de caracteres posibles (letras minúsculas y dígitos)
    caracteres = string.ascii_lowercase + string.digits
    # Elige 6 caracteres aleatorios de la lista
    id_aleatoria = ''.join(random.choices(caracteres, k=6))
    return id_aleatoria

# Ejemplo de uso:
print("ID de usuario aleatoria:")
print(random_user_id())
print("-" * 20)


def user_id_gen_by_user():

    try:
        num_caracteres = int(input("Introduce el número de caracteres para cada ID: "))
        num_ids = int(input("Introduce cuántas IDs quieres generar: "))
    except ValueError:
        return "Error: Por favor, introduce números enteros válidos."

    # Define el conjunto de caracteres posibles (letras mayúsculas, minúsculas y dígitos)
    caracteres = string.ascii_letters + string.digits
    lista_ids = []
    
    for _ in range(num_ids):
        id_generada = ''.join(random.choices(caracteres, k=num_caracteres))
        lista_ids.append(id_generada)
        
    return "\n".join(lista_ids) # Devuelve las IDs separadas por saltos de línea



def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"


