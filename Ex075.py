numeros = []
par = []
void = ''
cont = 0

for n in range(0, 4):
    perg = int(input(f"Digite o {n+1}º numero: "))
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
if 9 in tupla:
    print(f"O valor 9 apareceu {cont} vez(es)")
else:
    print(f"O valor 9 não foi digitado.")

if 3 in tupla:
    print(f"O número 3 apareceu na posição {tupla.index(3)}")
else:
    print("O valor 3 não foi encontrado em nenhuma posição.")

print("Os valores pares foram:", end='\033[1m | \033[m')

for par in tupla2:
    print(par, end='\033[1m | \033[m')
