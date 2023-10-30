lista = []
galera = []
void = ''
cont = 0
mai = []
men = []

while True:
    lista.append(str(input("Nome: ")))
    lista.append(int(input("Peso: ")))
    cont += 1
    galera.append(lista[:])

    print(void)

    perg = str(input("Quer continuar? [S/N] ")).upper()[0]

    if perg != 'S' and perg != 'N':
        print("Comando Desconhecido, tente novamente.")
        break

    if perg == 'N':
        break

print(void)

print(f"Ao todo, você cadastrou {cont} pessoas.")

print(void)

print(f"O maior peso foi Kg das seguintes pessoas: ")
print(f"O menor peso foi Kg das seguintes pessoas: ")
