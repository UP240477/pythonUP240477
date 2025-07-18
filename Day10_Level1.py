from typing import Counter

#NIVEL 1
# Iterar de 0 a 10 con un bucle for
print("Bucle for de 0 a 10:")
for i in range(11):
    print(i)

# Iterar de 0 a 10 con un bucle while
print("\nBucle while de 0 a 10:")
contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# Iterar de 10 a 0 con un bucle for
print("\nBucle for de 10 a 0:")
for i in range(10, -1, -1):
    print(i)

# Iterar de 10 a 0 con un bucle while
print("\nBucle while de 10 a 0:")
contador = 10
while contador >= 0:
    print(contador)
    contador -= 1

# Imprimir un triángulo de #
print("\nTriángulo:")
for i in range(1, 8):
    print('#' * i)

# Crear un patrón con bucles anidados
print("\nPatrón de rejilla:")
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print() # Salto de línea para la siguiente fila

# Imprimir una tabla de multiplicar
print("\nTabla de potencias:")
for i in range(11):
    print(f'{i} x {i} = {i * i}')

# Iterar a través de una lista de tecnologías
print("\nLista de tecnologías:")
lista_tech = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tecnologia in lista_tech:
    print(tecnologia)

# Imprimir solo los números pares de 0 a 100
print("\nNúmeros pares de 0 a 100:")
for i in range(101):
    if i % 2 == 0:
        print(i, end=' ')
print() # Salto de línea final

# Imprimir solo los números impares de 0 a 100
print("\nNúmeros impares de 0 a 100:")
for i in range(101):
    if i % 2 != 0:
        print(i, end=' ')
print() # Salto de línea final

