# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Introduzca su precio con dos decimales: ")
entero = precio[: precio.find(".")]
decimal = precio[precio.find(".") + 1 :]
print(entero, "euros con ", decimal, "céntimos.")
