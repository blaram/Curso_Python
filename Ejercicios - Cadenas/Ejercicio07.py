# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
email = input("Introduzca su email: ")
nuevoemail = email[: email.find("@")] + "@ceu.es"
print(nuevoemail)
