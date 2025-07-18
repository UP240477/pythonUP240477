# ---------------------------
# 1. Verificar si puede aprender a conducir
# ---------------------------
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    años_faltantes = 18 - edad
    if años_faltantes == 1:
        print("Te falta 1 año para poder aprender a conducir.")
    else:
        print(f"Te faltan {años_faltantes} años para poder aprender a conducir.")

# ---------------------------
# 2. Comparar tu edad con la mía
# ---------------------------
mi_edad = 25  # Cambia esto si tu edad es diferente
tu_edad = int(input("Ingresa tu edad: "))

if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print("Tienes 1 año más que yo.")
    else:
        print(f"Tienes {diferencia} años más que yo.")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print("Tengo 1 año más que tú.")
    else:
        print(f"Tengo {diferencia} años más que tú.")
else:
    print("Tenemos la misma edad.")

# ---------------------------
# 3. Comparar dos números
# ---------------------------
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")
