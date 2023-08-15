animal = "  peRRito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())  # Primera letra se pone en mayúscula
print(animal.title())  # Primeras letras de todas las palabras se ponen en mayúscula
print(animal.strip())  # Quita espacios
print(animal.lstrip())  # Quita espacios a la izquierda
print(animal.rstrip())  # Quita espacios a la derecha
print(animal.find("RR"))  # Busca una cadena de caracteres y nos devuelve el indice
print(animal.find("c"))  # Cuando no existe la cadena devuelve -1
print(
    animal.replace("eRR", "l")
)  # Reemplaza la cadena de la izquierda por la cadena de la derecha
print(
    "eRR" in animal
)  # Tambien busca la cadena de caracteres pero devuelve un booleano true o false
print("eRR" not in animal)  # Busca si la cadena no se encuentra en la variable
