num = int(input("Ingrese número entero: "))
lista = list(str(num))  
lista = [int(digito) for digito in lista]
suma = 0
for digito in lista:
    suma = suma + digito
print(f"Suma: {suma}")