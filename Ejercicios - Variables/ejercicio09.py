# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = input("Monto a invertir: ")
interes = input("Cual es el interés porcentual anual: ")
anios = input("Cuantos años: ")

capital = round(float(inversion) * (float(interes) / 100 + 1) ** int(anios), 2)
print("Capital final: ", capital)
# print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
