
#NIVEL 3
import countries_data
import countries
from typing import Counter


# --- Ejercicio 1: Países que contienen la palabra "land" ---
from countries import countries # Importa la lista de países

paises_con_land = []
for pais in countries:
    if 'land' in pais:
        paises_con_land.append(pais)

print("\nPaíses que contienen 'land':")
print(paises_con_land)


# --- Ejercicio 2: Invertir una lista de frutas con un bucle ---
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []

# Iteramos sobre la lista original y agregamos cada elemento al inicio de la nueva lista
for fruta in frutas:
    frutas_invertidas.insert(0, fruta)

print("\nLista de frutas invertida:")
print(frutas_invertidas)


# --- Ejercicios con countries_data.py ---

# 1. ¿Cuál es el número total de idiomas?
todos_los_idiomas = set()
for pais in countries_data.countriesdata:
    for idioma in pais['languages']:
        todos_los_idiomas.add(idioma)

print(f"\nEl número total de idiomas únicos en los datos es: {len(todos_los_idiomas)}")

# 2. Encuentra los diez idiomas más hablados
lista_completa_idiomas = []
for pais in countries_data.countriesdata:
    lista_completa_idiomas.extend(pais['languages'])

conteo_idiomas = Counter(lista_completa_idiomas)
print("\nLos 10 idiomas más hablados (por número de países que los hablan):")
print(conteo_idiomas.most_common(10))

# 3. Encuentra los 10 países más poblados
# Ordenamos la lista de países por población de mayor a menor
paises_ordenados_por_poblacion = sorted(countries_data.countriesdata, key=lambda pais: pais['population'], reverse=True)

print("\nLos 10 países más poblados del mundo:")
# Iteramos solo sobre los primeros 10 elementos de la lista ya ordenada
for i in range(10):
    pais = paises_ordenados_por_poblacion[i]
    print(f"{i+1}. {pais['name']}: {pais['population']:,} habitantes")