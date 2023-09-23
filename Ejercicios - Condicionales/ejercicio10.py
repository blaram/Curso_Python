# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Escoge una pizza 1. Vegetariana  2. No vegetariana")
pizza = input("Introduce el número: ")
if pizza == "1":
    print("Ingredientes: 1. Pimiento 2. Tofu")
    ingrediente = input("Ingrediente? ")
    print("Pizza vegetariana con mozarrella, toamate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes: 1. Peperoni 2. Jamós 3. Salmón")
    ingrediente = input("Ingrediente? ")
    print("Pizza no vegetariana con mozarrella, toamate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
