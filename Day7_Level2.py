#Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
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