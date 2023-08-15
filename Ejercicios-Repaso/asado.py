# Franco está organizando un asado con sus amigos y necesita de tu ayuda. 
# Para estimar cuánta carne necesita comprar, va a suponer que cada invitado come 0.7 Kg de carne. 
# Ayuda a Franco escribiendo un programa que permita al usuario ingresar la cantidad de invitados 
# y el precio de 1Kg. de carne, y muestre cuántos Kg de carne en total debe pedir al carnicero y 
# cuánto dinero necesita para pagar.

print("Ingrese la cantidad de invitados: ")
invitados = int(input())

print("Ingrese el precio por kg de la carne: ")
precio = float(input())

kg_totales = invitados * 0.7
precio_total = kg_totales * precio

print(f"Cantidad de kg totales a comprar: {kg_totales:2f}")
print(f"Precio total a pagar: {precio_total:2f}")