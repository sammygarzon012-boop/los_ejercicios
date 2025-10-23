caracter = input("Ingrese una letra: ").lower()  # Convertimos a minúscula para simplificar

if caracter in "aeiou":
    print("Es una vocal.")
else:
    print("Es una consonante.")
