mai = 0
men = 0

print()

for p in range(1, 6):

    pe = float(input(f"Digite o peso da {p}a pessoa: "))

    if p == 1:
        mai = pe
        men = pe
    else:
        if pe > mai:
            mai = pe
        if pe < men:
            men = pe

print()

print(f"O maior peso lido foi de {mai: .2f}Kg\nE o menor peso lido foi de {men: .2f}Kg")
