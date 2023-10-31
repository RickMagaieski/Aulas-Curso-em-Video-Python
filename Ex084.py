lista = []
galera = []
void = ''
mai = men = 0

while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Peso: ")))

    print(void)

    if len(galera) == 0:
        men = mai = lista[1]
    else:
        if lista[1] > mai:
            mai = lista[1]
        if lista[1] < men:
            men = lista[1]

    galera.append(lista[:])
    lista.clear()

    perg = str(input("Você quer continuar? [S/N] ")).upper()[0]

    print(void)

    if perg != 'S' and perg != 'N':
        print("Comando Inválido, tente novamente...")
        break
    if perg in 'N':
        break


print("-=" * 30)
print(f"A quantidade de pessoas cadastradas foi {len(galera)}")
print(f"O maior peso foi {mai}Kg das seguintes pessoas: ", end=' ')
for p in galera:
    if p[1] == mai:
        print(f"[{p[0]}]", end=' ')
print(f"\nO menor peso foi {men}Kg das seguintes pessoas: ", end=' ')
for p in galera:
    if p[1] == men:
        print(f"[{p[0]}]", end=' ')
