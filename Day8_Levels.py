# Crear un diccionario vacío llamado perro
perro = {}

# Agregar nombre, color, raza, patas y edad al diccionario del perro
perro['nombre'] = 'Fido'
perro['color'] = 'Marrón'
perro['raza'] = 'Labrador'
perro['patas'] = 4
perro['edad'] = 5

# Crear un diccionario de estudiante con los campos requeridos
estudiante = {
    'nombre': 'Carlos',
    'apellido': 'López',
    'género': 'Masculino',
    'edad': 20,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Resolución de problemas'],
    'país': 'México',
    'ciudad': 'Aguascalientes',
    'dirección': 'Calle Falsa 123'
}

# Obtener la longitud del diccionario del estudiante
longitud = len(estudiante)
print("Longitud del diccionario estudiante:", longitud)

# Obtener el valor de habilidades y verificar el tipo de dato
habilidades = estudiante['habilidades']
print("Habilidades:", habilidades)
print("Tipo de dato de habilidades:", type(habilidades))

# Modificar el valor de habilidades agregando una o dos habilidades
estudiante['habilidades'].append('Trabajo en equipo')
estudiante['habilidades'].append('Comunicación')
print("Habilidades actualizadas:", estudiante['habilidades'])

# Obtener las llaves del diccionario como lista
llaves = list(estudiante.keys())
print("Llaves del diccionario:", llaves)

# Obtener los valores del diccionario como lista
valores = list(estudiante.values())
print("Valores del diccionario:", valores)

# Convertir el diccionario a una lista de tuplas usando el método items()
tuplas = list(estudiante.items())
print("Diccionario como lista de tuplas:", tuplas)

# Eliminar uno de los elementos del diccionario (por ejemplo, la dirección)
del estudiante['dirección']
print("Diccionario después de eliminar 'dirección':", estudiante)

# Eliminar el diccionario completo del perro
del perro
# print(perro)  # Esto causaría un error si se descomenta, porque 'perro' ya no existe
