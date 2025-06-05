# Ejercicio 1

print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 % 4)             # modulus(%)
print(3 // 4)            # Floor division operator(//)

#Ejercicio 2

print("Carlos")
print("López")
print("Mexico")
print("I am enjoying 30 days of python")

#Ejercicio 3

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh','Python','Finland']))
print(type("Carlos"))
print(type("Juan, Judith, Karen, Valeria"))
print(type("Mexico"))

#Ejercicio1_Nivel 3

print(type({'name':'Carlos'}))   # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

import math

def distancia_euclidiana(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Puntos dados
punto1 = (2, 3)
punto2 = (10, 8)

# Calcular distancia
distancia = distancia_euclidiana(punto1[0], punto1[1], punto2[0], punto2[1])

print(f"Punto 1: {punto1}")
print(f"Punto 2: {punto2}")
print(f"Distancia Euclidiana: {distancia:.2f}")
