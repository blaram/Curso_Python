# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha = input("Ingrese su fecha de nacimiento en este formato (dd/mm/aaaa)")
dia = fecha[:2]
mes = fecha[3:5]
anio = fecha[6:]
print("Día ", dia)
print("Mes ", mes)
print("Año ", anio)

dia = fecha[: fecha.find("/")]
mesanio = fecha[fecha.find("/") + 1 :]
mes = mesanio[: mesanio.find("/")]
anio = mesanio[mesanio.find("/") + 1 :]

print("Día ", dia)
print("Mes ", mes)
print("Año ", anio)
