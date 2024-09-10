texto = input("Ingrese palabra: ")
texto = texto.lower()
texto_invertido = texto[::-1]
if texto == texto_invertido:
    print("La palabra es un Palíndromo")
else:
    print("La palabra no es un Palíndromo")