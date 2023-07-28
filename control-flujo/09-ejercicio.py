print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")
operacion = ""
n1 = input("Ingresa número: ")
n1 = int(n1)

while True:
    print("Ingresa operación: ")
    operacion = input("$ ")
    if operacion.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    n2 = int(n2)

    if operacion == "suma":
        resultado = n1 + n2
    elif operacion == "multi":
        resultado = n1 * n2
    elif operacion == "div":
        resultado = n1 / n2
    else:
        resultado = n1 - n2
        # resultado = int(resultado)
    n1 = resultado
    print("El resultado es ", resultado)
