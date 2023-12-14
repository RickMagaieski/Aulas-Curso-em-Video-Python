som = 0
cont = 0

print()

for n in range(1, 7):
    p = int(input(f"Digite o {n}o valor: "))
    if p % 2 == 0:
        som += p
        cont += 1

print()

if som and cont == 0:
    print("Voce nao informou nenhum numero par, logo a soma deu 0")
else:
    print(f"Voce informou {cont} numeros pares e o resultado final da soma foi {som}")
