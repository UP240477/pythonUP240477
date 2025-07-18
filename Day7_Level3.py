#Level 3
print("Level 3")
age = [22, 19, 24, 25, 26, 24, 25, 24]

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
