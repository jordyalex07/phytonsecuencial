numero_como_cadena= input("Escribe un numero")
numero = float(numero_como_cadena)
if numero == 0:
    print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")
