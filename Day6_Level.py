# Crear una tupla vacía
empty_tuple = ()

# Crear tuplas con nombres de hermanos y hermanas
sisters = ("Karen", "Valeria")
brothers = ("Juan", "Abraham", "Daniel", "Eduardo", "Christopher")

# Unir las tuplas de hermanos y hermanas
siblings = sisters + brothers

# Contar cuántos hermanos hay
print("Número de hermanos:", len(siblings))

# Agregar padres a la tupla
family_members = siblings + ("Papá", "Mamá")

# Mostrar los miembros de la familia
print("Miembros de la familia:", family_members)

# Paso 4: Desempaquetar hermanos y padres
*all_siblings, father, mother = family_members
print("Hermanos:", all_siblings)
print("Padre:", father)
print("Madre:", mother)

# Paso 5: Crear tuplas de comida
fruits = ("manzana", "naranja", "plátano")
vegetables = ("zanahoria", "lechuga", "pepino")
animal_products = ("leche", "queso", "huevo")

# Paso 6: Unir todas las tuplas de comida
food_stuff_tp = fruits + vegetables + animal_products
print("Tupla de comida:", food_stuff_tp)

# Paso 7: Convertir la tupla en lista
food_stuff_lt = list(food_stuff_tp)
print("Lista de comida:", food_stuff_lt)

# Paso 8: Sacar el/los elemento(s) del medio
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print("Elemento(s) del medio:", middle_items)

# Paso 9: Sacar los primeros 3 y últimos 3 elementos
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("Primeros 3:", first_three)
print("Últimos 3:", last_three)

# Paso 10: Borrar completamente la tupla
del food_stuff_tp
# print(food_stuff_tp)  # Esto daría error porque ya no existe

# Paso 11: Verificar si un país está en la tupla de países nórdicos
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("¿Estonia es país nórdico?", 'Estonia' in nordic_countries)
print("¿Iceland es país nórdico?", 'Iceland' in nordic_countries)