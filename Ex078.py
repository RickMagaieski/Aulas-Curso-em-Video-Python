lista = []
lista2 = []
lista3 = []
void = ''

for num in range(0, 5):
    lista.append(int(input(f"Digite um número na posição {num}: ")))

for i, valor in enumerate(lista):
    if valor == max(lista):
        lista2.append(i)
    if valor == min(lista):
        lista3.append(i)

print(f"Você digitou os seguintes valores: {lista}")
print(void)
print(f"O maior valor desta lista é o valor {max(lista)}, encontrado na(s) seguinte(s) posição(ões): {lista2}")
print(f"O menor valor desta lista é o valor {min(lista)}, encontrado na(s) seguinte(s) posição(ões): {lista3}")
