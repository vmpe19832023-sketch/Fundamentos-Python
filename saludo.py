nombre = input("¿Cuál es tu nombre? ")
anio_nacimiento = input("¿En qué año naciste? ")
anio_actual = 2026
edad = anio_actual - int(anio_nacimiento)
if edad >= 18:
    print("Eres mayor de edad")
elif edad>=0:
    print("Eres menor de edad")
else:
    print("Fecha inválida, ¿aun no naces?")
print(f"Mi nombre es {nombre}, mi año de nacimiento es {anio_nacimiento} y mi edad es {edad}.")