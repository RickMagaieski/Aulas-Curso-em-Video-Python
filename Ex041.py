print()

ano = int(input("Digite o ano de nascimento do atleta: "))

conta = 2023 - ano

print()

if conta <= 9:
    print(f"O atleta tem {conta} anos.\nPortanto ele e um atleta MIRIM")
elif conta <= 14:
    print(f"O atleta tem {conta} anos.\nPortanto ele e um atleta INFANTIL")
elif conta <= 19:
    print(f"O atleta tem {conta} anos.\nPortanto ele e um atleta JUNIOR")
elif conta <= 25:
    print(f"O atleta tem {conta} anos.\nPortanto ele e um atleta SENIOR")
elif conta > 25:
    print(f"O atleta tem {conta} anos.\nPortanto ele e um atleta MASTER")
