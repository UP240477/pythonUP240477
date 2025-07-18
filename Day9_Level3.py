
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
