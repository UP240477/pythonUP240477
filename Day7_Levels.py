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

#Level 2
print("Level 2")
# 1. Unión de A y B
print(A.union(B))  # o A | B

# 2. Intersección
print(A.intersection(B))  # o A & B

# 3. ¿A es subconjunto de B?
print(A.issubset(B))  # True

# 4. ¿A y B son disjuntos?
print(A.isdisjoint(B))  # False

# 5. Unir A con B y B con A
print(A.union(B))
print(B.union(A))

# 6. Diferencia simétrica (elementos que están en A o B pero no en ambos)
print(A.symmetric_difference(B))  # o A ^ B

# 7. Eliminar los sets completamente
del A
del B

print("-"*50);

#Level 3
print("Level 3")

# 1. Convertir a set y comparar longitudes
age_set = set(age)
print("Longitud de la lista:", len(age))     # 8
print("Longitud del set:", len(age_set))     # 5

# 2. Diferencias entre string, list, tuple y set
'''
- string: texto, inmutable, entre comillas. Ej: "Hola"
- list: colección ordenada y mutable. Ej: [1, 2, 3]
- tuple: colección ordenada pero inmutable. Ej: (1, 2, 3)
- set: colección no ordenada, sin elementos duplicados. Ej: {1, 2, 3}
'''

# 3. ¿Cuántas palabras únicas hay en la oración?
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Palabras únicas:", unique_words)
print("Número de palabras únicas:", len(unique_words))  # Salida: 10


