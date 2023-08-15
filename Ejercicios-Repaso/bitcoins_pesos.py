# Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos 
# equivalen hoy los Bitcoins (BTC) que encontró guardados en un disco rígido viejo. 
# El usuario del programa debe ingresar una cantidad en Bitcoins.


val_bit = float(input("Ingrese el valolr del bitcoin actual: "))

print("Ingrese la cantidad de Bitcoins: ")
bitcoins = float(input())

cant = bitcoins * val_bit
print(f"Cantidad de pesos argentinos equivalentes a {bitcoins} hoy en dia: ")
