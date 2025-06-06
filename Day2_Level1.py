#Ejercicios nivel 1

First_name='Carlos' #Declarar variable primer nombre
Last_name='López' #Declarar variable apellido
Full_name='Carlos Emilio López Martin' #Declarar variable nombre
Country='Mexico' #Declarar variable pais
City='Aguascalientes' #Declarar variable ciudad
Age='22' #Declarar variable edad
Year='2025' #Declarar variable año
Is_married='yes' #Declarar variable
Is_true='yes' #Declarar variable 
Is_light='' #Declarar variable 
Second_name, dog_name, girlfriend = 'Emilio','Peque','Isabel' #Declarar variables en una misma linea

print(type(Full_name))
print(len(First_name))
print(len(Last_name))

#Ejercicios nivel 2

num_one=5
num_two=4
Variable_total=num_one+num_two
Variable_diff=num_one-num_two
Variable_product=num_two*num_one
Variable_division=num_one/num_two
Variable_remainder=num_two%num_one
Variable_exp= num_one ** num_two
Floor_division= num_one // num_two

print("\n" + "=" * 40)
radius = 30  # metros
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius


print(f"Para el circulo con radio {radius} metros:")
print(f"Area del circulo = {area_of_circle:.2f}  metros cuadrados")
print(f"Circunferencia del Circulo = {circum_of_circle:.2f} metros")
print()

user_radius = float(input("Introduce el radio del circulo en metros: "))
user_area = 3.14 * user_radius ** 2

print(f"Para el circulo con radio {user_radius} metros:")
print(f"Area = {user_area:.2f} metros cuadrados")

print("\n" + "=" * 40)
print("Please provide the following information:")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("\n" + "=" * 40)
print("COLLECTED INFORMATION:")
print("=" * 40)
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")