
#NIVEL 3

import countries_data
from typing import Counter

# Función que comprueba si un número es primo
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Función que comprueba si todos los elementos de una lista son únicos
def are_all_unique(lst):
    return len(lst) == len(set(lst))

# Función que comprueba si todos los elementos son del mismo tipo
def are_all_same_type(lst):
    if not lst:
        return True # Una lista vacía cumple la condición
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

# Función que comprueba si un string es un nombre de variable válido en Python
def is_valid_variable(name):
    return name.isidentifier()

# Función que devuelve los idiomas más hablados
def most_spoken_languages(n=10):
    all_languages = []
    for country in countries_data.countriesdata:
        all_languages.extend(country['languages'])
    
    language_counts = Counter(all_languages)
    return language_counts.most_common(n)

# Función que devuelve los países más poblados
def most_populated_countries(n=10):
    sorted_countries = sorted(countries_data.countriesdata, key=lambda x: x['population'], reverse=True)
    
    # Extraer solo el nombre y la población para una salida más limpia
    top_countries = []
    for country in sorted_countries[:n]:
        top_countries.append({'country': country['name'], 'population': country['population']})
        
    return top_countries