numeros = []
par = []
void = ''
cont = 0

for n in range(0, 4):
    perg = int(input(f"Digite o numero para posição {n}º: "))
    numeros.append(perg)
    if perg == 9:
        cont += 1
    if perg % 2 == 0:
        par.append(perg)

tupla = tuple(numeros)
tupla2 = tuple(par)
print(void)

print(f"Os números digitados foram os seguintes: {tupla}")
print(void)
print(f"O valor 9 apareceu {cont} vez(es)")

if 3 in tupla:
    print(f"O número 3 apareceu na posição {tupla.index(3)}")
else:
    print("O valor 3 não foi encontrado em nenhuma posição")

print("Os valores pares foram:", end=' ')

for par in tupla2:
    print(par, end=' ')
