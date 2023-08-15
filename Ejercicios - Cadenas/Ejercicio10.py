# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
productos = input("Ingrese los productos separados por una coma")
cesta = productos.replace(",", "\n")
print(cesta)

# Otra forma
print("\n".join(productos.split(",")))
