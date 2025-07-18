# ---------------------------
# 4. Asignar calificación por puntaje
# ---------------------------
puntaje = int(input("Ingresa tu puntaje: "))

if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje <= 79:
    print("Calificación: B")
elif 60 <= puntaje <= 69:
    print("Calificación: C")
elif 50 <= puntaje <= 59:
    print("Calificación: D")
elif 0 <= puntaje <= 49:
    print("Calificación: F")
else:
    print("Puntaje no válido.")

# ---------------------------
# 5. Determinar la estación del año
# ---------------------------
mes = input("Ingresa el mes: ").capitalize()

if mes in ['Septiembre', 'Octubre', 'Noviembre']:
    print("La estación es Otoño.")
elif mes in ['Diciembre', 'Enero', 'Febrero']:
    print("La estación es Invierno.")
elif mes in ['Marzo', 'Abril', 'Mayo']:
    print("La estación es Primavera.")
elif mes in ['Junio', 'Julio', 'Agosto']:
    print("La estación es Verano.")
else:
    print("Mes no válido.")

# ---------------------------
# 6. Verificar si una fruta está en la lista
# ---------------------------
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta_nueva = input("Ingresa una fruta: ").lower()

if fruta_nueva in frutas:
    print("Esa fruta ya existe en la lista.")
else:
    frutas.append(fruta_nueva)
    print("Fruta añadida. Lista actualizada:", frutas)
