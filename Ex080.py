lista = []
void = ''

for q in range(0, 5):
    perg = int(input("Digite um valor: "))
    if len(lista) == 0 or perg > lista[-1]:
        lista.append(perg)
        print("Valor inserido no final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if perg <= lista[pos]:
                lista.insert(pos, perg)
                print(f"Valor inserido na posição {pos}")
                break
            pos += 1

print(void)
print(lista)
