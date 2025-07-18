#NIVEL 2

# Sumar todos los números del 0 al 100
suma_total = 0
for i in range(101):
    suma_total += i
print(f"La suma de todos los números es {suma_total}.")

# Sumar todos los pares y todos los impares del 0 al 100
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print(f"La suma de todos los pares es {suma_pares}. Y la suma de todos los impares es {suma_impares}.")