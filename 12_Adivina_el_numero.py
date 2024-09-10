import random 
num = random.randint(1, 10)
usuario = int(input("Adivina el número, ingresa un número del 1 al 10: "))
if num == usuario:
    print("Adivinaste")
else:
    print("Sigue intentando")