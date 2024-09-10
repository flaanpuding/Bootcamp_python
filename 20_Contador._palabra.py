palabra = input("Ingrese texto: ")
contador_palabra = palabra.split()
count = 0
for frase in contador_palabra:
    count = count+1
print(f"La cantidad de pabras es: {count}")