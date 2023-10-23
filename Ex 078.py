lista = []
posmai = []
posmen = []
void = ''

for p in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {p}: ")))

for i, valor in enumerate(lista):
    if valor == max(lista):
        posmai.append(i)
    if valor == min(lista):
        posmen.append(i)

print(void)
print(f"Os valores digitados foram esses: {lista}")
print(void)

print(f"O maior valor foi o valor {max(lista)} na(s) posição(ões):", end=' ')
for ar in posmai:
    print(ar, end='... ')

print(f"\nO menor valor foi o valor {min(lista)} na(s) posição(ões):", end=' ')
for arr in posmen:
    print(arr, end='... ')

print(void)
