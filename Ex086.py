matriz = [[], [], [],
          [], [], [],
          [], [], []]
void = ''
cont = 0

for m in range(0, 9):
    matriz[m].append(int(input(f"Digite um número para: ")))

print("-=" * 30)

for linha in matriz:
    for valor in linha:
        print(f"[  {valor}  ]", end=' ')
        if valor > 10:
            print(f"[ {valor} ]", end=' ')
        cont += 1
    if cont % 3 == 0:
        print()
