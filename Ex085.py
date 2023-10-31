numeros = [[], []]
void = ''

for num in range(1, 8):
    perg = int(input(f"Digite o {num}º valor: "))
    if perg % 2 == 0:
        numeros[0].append(perg)
    else:
        numeros[1].append(perg)

print(void)

numeros[0].sort()
numeros[1].sort()

print(f"Números pares: {numeros[0]}")
print(f"Números ímpares: {numeros[1]}")
