# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

deposito = float(input("Monto a depositar: "))
primer = (1 + 0.04) * deposito
print("Balance primer año: ", round(primer, 2))
segundo = (1 + 0.04) * primer
print("Balance segundo año: ", round(segundo, 2))
tercer = (1 + 0.04) * segundo
print("Balance tercer año: ", round(tercer, 2))
