lista = []
void = ''

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    perg = str(input("Deseja continuar? [S/N] ")).upper()

    if perg != 'S' and 'N':
        print("Comando desconhecido, tente novamente!")
        break
    elif perg == 'N':
        break

print(void)
lista.sort(reverse=True)

print(f"Você digitou {len(lista)} elementos.")
print(f"A lista gerada a partir dos números digitados foi esta: {lista}")
if 8 in lista:
    print("O número 8 está na lista!")
else:
    print("O número 8 não está na lista...")
