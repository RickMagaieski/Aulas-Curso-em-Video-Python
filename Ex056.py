media = 0
contm = 0
nom = []

mai = 0
men = 0

print()

for p in range(1, 5):
    print("=" * 10, f"{p}a Pessoa", "=" * 10)
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: "))[0].upper()

    media += idade / 4

    if p == 1:
        mai = idade
        men = idade
    else:
        if idade > mai:
            mai = idade
            if sexo == "M":
                nom.append(nome)

    if sexo == "F":
        contm += 1

    print()

print(f"A media de idade do grupo e de {media: .1f} anos")
for n in nom:
    print(f"O homem mais velho tem {mai} e se chama {n}")
print(f"Ao todo sao {contm} mulheres com menos de 20 anos")
