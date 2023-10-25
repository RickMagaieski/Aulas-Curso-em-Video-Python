lista = []
imp = []
par = []
void = ''

while True:
    n = int(input("Digite um número: "))
    lista.append(n)
    perg = str(input("Deseja continuar? [S/N] ")).upper()

    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        imp.append(n)

    if perg != 'S' and perg != 'N':
        print("Comando Inválido! Tente novamente.")
        break
    elif perg == 'N':
        break

lista.sort()

print("\nEsta é a sua lista principal já ordenada:", end=' ')
for li in lista:
    if li == lista[-1]:
        print(li, end='...')
    else:
        print(li, end=', ')
print(void)

if len(par) > 0:
    print("\nEsta é a sua lista apenas com números pares:", end=' ')
    for pa in par:
        if pa == par[-1]:
            print(pa, end='...')
        else:
            print(pa, end=', ')
else:
    print("\nNenhum número par foi digitado.")

if len(imp) > 0:
    print("\nEsta é a sua lista apenas com número ímpares:", end=' ')
    for impar in imp:
        if impar == imp[-1]:
            print(impar, end='...')
        else:
            print(impar, end=', ')
else:
    print("\nNenhum número ímpar foi digitado.")

print(void)
