matriz = [[], [], [],
          [], [], [],
          [], [], []]
void = ''
cont = 0
somapar = 0
seglinha = 0
somacolu = 0

for m in range(0, 9):
    perg = int(input(f"Digite um número para: "))
    matriz[m].append(perg)

    if m == 2 or m == 5 or m == 8:
        somacolu += perg
    if perg % 2 == 0:
        somapar += perg

    seglinha = matriz[3] + matriz[4] + matriz[5]

print("-=" * 30)

for linha in matriz:
    for valor in linha:
        print(f"[  {valor}  ]", end=' ')
        if valor > 10:
            print(f"[ {valor} ]", end=' ')
        cont += 1
    if cont % 3 == 0:
        print()

print("-=" * 30)

print(f"A soma de todos os valores pares é: {somapar}")
print(f"A soma de todos os valores da terceira coluna: {somacolu}")
print(f"O maior valor da segunda linha é: {max(seglinha)}")
