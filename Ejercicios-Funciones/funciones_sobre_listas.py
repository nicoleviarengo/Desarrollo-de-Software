# Funciones para operar sobre una lista
# Generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:

# Muestre la lista

# El usuario ingresa debe ingresar un valor un valor. 
# El programa debe informar cuántos valores de la lista son mayores a dicho valor, para eso debe utilizar una función.
# La función debe recibir como argumentos la lista y un entero, y debe retornar la cantidad de valores de la lista mayores a dicho entero.

# Crear una función que calcule el promedio de la lista y utilizarla.

# Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne.

lista = []

import random

def carga():
    for v in range(10):
        num=(random.randrange(10, 20, 1))
        lista.append(num)
    print(lista)

def proceso(valor):
    
     cont = 0
     for elem in lista:
        if elem > valor:
            cont += 1
     print(f"Hay {cont} mayores al numero ingresado")
    

def promedio():
    cont = 0
    suma=0
    while len(lista)!=0:
         desapilada = lista.pop()
         cont +=1
    suma = suma + desapilada
    prom = suma/cont 
    print(f"Promedio de valores de la lista: {prom}")

def mayorYmenor():
    valorDes = lista.pop()
    min(valorDes)
    max(valorDes)
    print(f"Menor valor de la lista: {min}")
    print(f"Mayor valor de la lista: {max}")

carga()
print("Ingrese un valor: ")
valor = int(input())
proceso(valor)
promedio()
mayorYmenor()