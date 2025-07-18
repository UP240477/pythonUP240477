# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Longitud del set it_companies
print(len(it_companies))  # Salida: 7

# 2. Agregar 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insertar múltiples compañías a la vez
it_companies.update(['Spotify', 'Intel', 'Adobe'])
print(it_companies)

# 4. Eliminar una compañía (por ejemplo, 'IBM')
it_companies.remove('IBM')  # Lanza error si no existe
print(it_companies)

# 5. Diferencia entre remove y discard
# - remove() lanza error si el elemento no está en el set.
# - discard() NO lanza error si el elemento no está.
it_companies.discard('XYZ')  # No hace nada
print("-"*50);



