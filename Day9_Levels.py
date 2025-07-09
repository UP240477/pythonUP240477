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

# ---------------------------
# 7. Análisis del diccionario de persona
# ---------------------------
persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Space street',
        'codigo_postal': '02210'
    }
}

# Verificar si tiene 'habilidades' y mostrar la del medio
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    medio = len(habilidades) // 2
    print("Habilidad del medio:", habilidades[medio])

    # Verificar si tiene 'Python'
    if 'Python' in habilidades:
        print("Tiene la habilidad de Python: Sí")
    else:
        print("Tiene la habilidad de Python: No")

    # Clasificación según habilidades
    if set(habilidades) == {'JavaScript', 'React'}:
        print("Es un desarrollador Frontend")
    elif all(h in habilidades for h in ['Node', 'Python', 'MongoDB']):
        print("Es un desarrollador Backend")
    elif all(h in habilidades for h in ['React', 'Node', 'MongoDB']):
        print("Es un desarrollador Fullstack")
    else:
        print("Título desconocido")

# Verificar si está casado y vive en Finlandia
if persona['casado'] and persona['pais'] == 'Finlandia':
    nombre_completo = f"{persona['nombre']} {persona['apellido']}"
    print(f"{nombre_completo} vive en Finlandia. Está casado.")
