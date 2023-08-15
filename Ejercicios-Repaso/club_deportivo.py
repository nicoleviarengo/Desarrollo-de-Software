# Un club deportivo tiene 4 categorías de asociados según la edad:

# - infantiles (desde 13 a 15 años)
# - cadetes (a partir de los 15 y hasta 17)
# - juveniles (desde los 17 hasta los 19)
# - mayores (de 19 años en adelante)

# Escriba un programa que permita al usuario ingresar el nombre y la edad 
# de un socio y muestre su el nombre de la categoría en la que le corresponde estar.

print("Ingrese el nombre: ")
nombre = str(input())
print("Ingrese la edad: ")
edad = int(input())

print(f"Nombre: {nombre}")
if edad == 13 or edad == 14 or edad == 15:
    print(f"Categoria: Infantile")
elif edad == 16 or edad == 17:
    print("Categoria: Cadete")
elif edad == 18 or edad == 19:
    print("Categoria: Juvenil")
elif edad > 19:
    print("Categoria: Mayor")