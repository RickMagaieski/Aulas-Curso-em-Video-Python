lista = []
lista2 = []
lista3 = []
void = ''

for num in range(0, 5):
    perg = int(input(f"Digite um número na posição {num}: "))
    lista.append(perg)
maxv = max(lista)
minv = min(lista)

for i, valor in enumerate(lista):
    if valor == maxv:
        lista2.append(i)
    if valor == minv:
        lista3.append(i)

print(f"Você digitou os seguintes valores: {lista}")
print(void)

if lista2 > [0]:
    print(f"O maior valor desta lista é o valor {maxv}, encontrado nas seguintes posições: {lista2}")
if lista3 > [0]:
    print(f"O menor valor desta lista é o valor {minv}, encontrado nas sequintes posições: {lista3}")
else:
    print(f"O maior valor desta lista é o valor {maxv}, encontrado na posição {lista.index(maxv)}")
    print(f"O menor valor desta lista é o valor {minv}, encontrado na posição {lista.index(minv)}")
