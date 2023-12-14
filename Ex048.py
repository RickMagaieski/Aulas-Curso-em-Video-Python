cont = 0
cont2 = 0
som = 0
som2 = 0

for n in range(1, 501):
    if n % 3 == 0 and n % 2 != 0:
        cont += 1
        som += n
    elif n % 4 == 0 and n % 2 == 0:
        cont2 += 1
        som2 += n
print()

print(f"A soma de todos os {cont} valores multiplos de tres impares solicitados foi de {som}")
print(f"A soma de todos os {cont2} valores multiplos de quatro pares solicitados foi de {som2}")
