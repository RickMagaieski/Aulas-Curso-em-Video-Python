lista = []
void = ''

while True:
    perg = int(input("Digite um valor: "))
    if perg in lista:
        print("Valor duplicado, não irei adicionar.")
    else:
        lista.append(perg)
    perg2 = str(input("Deseja continuar? [S/N] ")).upper()

    if perg2 != 'S' and perg2 != 'N':
        print("Comando Desconhecido, tente novamente!")
        break
    if perg2 == 'N':
        break

print(void)
print(f"Os valores digitados foram os valores: {sorted(lista)}")
