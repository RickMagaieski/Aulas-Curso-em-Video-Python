n = 0
som = 0
cont = 0

print()

while n != 999:

    n = int(input("Digite um numero (digite 999 para parar): "))

    if n != 999:

        cont += 1
        som += n

print()

print(f"Foram digitados {cont} valores que somados deram {som}")
