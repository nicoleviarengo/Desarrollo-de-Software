# Durante los 5 días de una semana se tomaron mediciones de temperatura en la ciudad. 
# Se desea conocer cuál fue la temperatura promedio de la semana. 
# Escriba un programa que permita calcularla a partir de 5 valores de temperatura que ingresará el usuario.

lista = []

def Promedio(lista):
    suma = 0
    while len(lista)!=0:
        x = lista.pop()
        suma = suma + x
    prom = suma / 5
    print(f"Temperaturas: {x}")
    print(f"Promedio de temperaturas: {prom}")

print("Ingrese las temperaturas de la semana: ")
for c in range(5):
    temp = int(input())
    lista.append(temp)

Promedio(lista)