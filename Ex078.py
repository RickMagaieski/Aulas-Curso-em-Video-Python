lista = []
void = ''

for num in range(0, 5):
    perg = int(input(f"Digite um número na posição {num}: "))
    lista.append(perg)
print(f"Você digitou os seguintes valores: {lista}")
print(void)
print(f"O maior valor desta lista é o valor {max(lista)}, encontrado nas seguintes posições: ")
print(f"O menor valor desta lista é o valor {min(lista)}, encontrado nas sequintes posições: ")
print(void)
print(lista.index(max(lista)))
print(lista.index(min(lista)))
