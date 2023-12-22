print("=" * 21)

print(" CADASTRE UMA PESSOA")

print("=" * 21)

print()

hom = 0
mul = 0
dezoi = 0

while True:
    print("=" * 14)

    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).upper()

    o = ''

    print("=" * 14)
    print()

    if idade > 18:
        dezoi += 1
    if idade < 20 and sexo == "F":
        mul += 1
    if sexo == "M":
        hom += 1

    while True:

        perg = str(input("Quer continuar ? [S/N] "))[0].upper()

        print()

        if perg == "N":
            o = 'N'
            break
        elif perg != "S" and "N":
            print("Comando Desconhecido. Tente novamente!")
        elif perg == "S":
            break

    if o == 'N':
        break

print()

print(f"Total de pessoas com mais de 18 anos: {dezoi}")
print(f"Ao todo temos pelo menos {hom} homem(ns) cadastrado(s)")
print(f"E temos {mul} mulher(es) com menos de 20 anos")
