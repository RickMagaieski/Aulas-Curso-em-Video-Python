mai = 0
men = 0

print()

for p in range(1, 8):
    ano = int(input(f"Digite o ano da {p}a pessoa: "))

    if 2023 - ano > 18:
        mai += 1
    else:
        men += 1

print()

print(f"Ao todo tivemos {mai} maiores de idade\nE {men} pessoas menores de idade")
