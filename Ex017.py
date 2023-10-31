from math import hypot

cateto1 = float(input("Comprimento do cateto oposto: "))
cateto2 = float(input("Comprimento do cateto adjacente: "))

print(f"A hipotenusa vai medir: {(cateto1 ** 2 + cateto2 ** 2) ** (1/2):.2f}")
