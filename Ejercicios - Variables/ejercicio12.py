# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
vendidas = int(input("Barras vendidas que no son del día: "))
precio = 3.49
descuento = 0.6
print("El precio de la barra es: ", precio)
print("El descuento es ", descuento)
total = round(vendidas * precio * (1 - descuento), 2)
print("El total es: ", total)
