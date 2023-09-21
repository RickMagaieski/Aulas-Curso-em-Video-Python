#Treino de TUPLAS: Ex072 - Número por extenso

"""numeros = ("UM", "DOIS", "TRES", "QUATRO", "CINCO",
    "SEIS", "SETE", "OITO", "NOVE", "DEZ",
    "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE",
    "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
void = ''

while True:
    perg = int(input("Digite um número entre 0 e 20: "))
    if perg > 20 or perg < 0:
        print("Erro, comando desconhecido, tente novamente!")
        print(void)
    else:
        print("O número digitado foi o numero", numeros[perg - 1])
        break"""
import random

#Treino de TUPLAS: Ex073 - Tuplas com Universidades Americanas

"""void = ''
univer = ("HARVARD UNIVERSITY", "STANFORD UNIVERSITY", "MASSACHUSETTS INSTITUTE OF TECHNOLOGY (MIT)",
    "CALIFORNIA INSTITUTE OF TECHNOLOGY (CALTECH)", "PRINCETON UNIVERSITY", "YALE UNIVERSITY",
    "UNIVERSITY OF CHICAGO", "COLUMBIA UNIVERSITY", "UNIVERSITY OF PENNSYLVANIA",
    "JOHNS HOPKINS UNIVERSITY", "NORTHWESTERN UNIVERSITY", "DUKE UNIVERSITY",
    "UNIVERSITY OF CALIFORNIA, BERKELEY (UC BERKELEY)", "UNIVERSITY OF CALIFORNIA, LOS ANGELES (UCLA)",
    "UNIVERSITY OF MICHIGAN, ANN ARBOR", "UNIVERSITY OF NORTH CAROLINA AT CHAPEL HILL",
    "CARNEGIE MELLON UNIVERSITY", "UNIVERSITY OF CALIFORNIA, SAN DIEGO (UCSD)",
    "NEW YORK UNIVERSITY (NYU)", "UNIVERSITY OF VIRGINIA")

print("\033[4m\033[1mAs primeiras cinco melhores universidades são:\033[m")
print(void)
for u in range(0, len(univer[0:5])):
    print(f"{univer[u]}")

print(void)
print(void)

print("\033[4m\033[1mAs últimas quatro melhores universidades são:\033[m")
print(void)
for u in univer[-4:]:
    print(f"{u}")

print(void)
print(void)

print("\033[4m\033[1mUniversidades em ordem alfabética:\033[m")
print(void)
for s in sorted(univer):
    print(s)

print(void)
print(void)

for loc, uni in enumerate(univer):
    if 'HARVARD' in uni:
        print(f"\033[1mHARVARD\033[m está na \033[1m{loc + 1}ª\033[m posição")
    else:
        print("Universidade não encontrada")"""




#Treino de TUPLAS: Ex074 - Maior e Menor Valores em Tupla

"""from random import randint

ale = []
void = ''

for r in range(1, 5):
    rand = randint(0, 10)
    ale.append(rand)

print(f"\033[1mValores sorteados:\033[m {tuple(ale)}")
print(void)
print(f"\033[1mO maior valor dentro da tupla é:\033[m {max(tuple(ale))}")
print(f"\033[1mO menor valor dentro da tupla é:\033[m {min(tuple(ale))}")"""




#Treino de TUPLAS: Ex075 - Análise de Dados em Tuplas

"""lista = []
cont = 0
void = ''
cont2 = 0


for v in range(1, 5):
    perg = int(input("Digite um número: "))
    lista.append(perg)
    if perg == 9:
        cont += 1
    if perg % 2 == 0:
        cont2 += 1


tupla = tuple(lista)

print(f"Você digitou os seguintes valores: {tupla}")
print(void)
print(f"O número 9 apareceu {cont} vezes")
if 3 in tupla:
    print(f"O primeiro numero três aparece na {tupla.index(3) + 1}ª posição")
else:
    print("Não foi digitado nenhum numero 3")
print(f"Foram digitados {cont2} numeros pares")"""




#Treino de TUPLAS: Ex076 - Lista de Preços com Tuplas

"""contprice = 0
void = ''
propre = ('Filtro de Linha', 45.12,
         'Mouse', 35.65 ,
         'Teclado', 35.54,
         'Monitor', 480.22,
         'Gabinete', 200.12,
         'Placa de Video', 2250.32,
         'Ssd', 92.30,
         'Placa Mãe', 102.21,
         'Fonte', 305.12,
         'Fone', 82.32,
         'Memórias RAM', 32.14,
         'Processador', 63.70)


print(void)
print("=" * 40)
print(f"{'My Computer Price':>25}")
print("=" * 40)

for c in range(0, len(propre)):
    if c % 2 == 0:
        print(f"{propre[c]:.<30}R$", end=' ')
    else:
        print(f"{propre[c]:>7.2f}")
        contprice += propre[c]

print("=" * 40)
print(void)
print(f"Total: {contprice:.2f}")"""




#Treino de TUPLAS: Ex077 - Contando Vogais em Tupla

"""propre = 'Filtro de Linha', 'Mouse', 'Teclado', 'Monitor', 'Gabinete', 'Placa de Video', 'Ssd', 'Placa Mãe'\
    , 'Fonte', 'Fone', 'Memórias RAM', 'Processador'

for s in propre:
    print(f"\nEm \033[1m{s}\033[m temos: ", end='')
    for letra in s:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')"""





#Treino de LISTAS: Ex078 - Maior e Menor valores na Lista

"""lista = []
lista2 = []
lista3 = []
void = ''

for cont in range(0, 5):
    perg = int(input(f"Digite um número para posição {cont}: "))
    lista.append(perg)

for i, c in enumerate(lista):
    if c == max(lista):
        lista2.append(i)
    if c == min(lista):
        lista3.append(i)

print(void)
print(f"Esses são os valores que você digitou: {lista}")
print(void)
print(f"O maior valor digitado foi o número {max(lista)} que está na(s) posição(ções): {lista2}")
print(f"O menor valor digitado foi o número {min(lista)} que está na(s) posição(ções): {lista3}")"""




#Treino de LISTAS: Ex079 - Valores únicos em uma lista

"""lista = []

while True:
    perg = int(input("Digite um número: "))
    if perg not in lista:
        lista.append(perg)
    else:
        print("O valor não foi adicionado pois ele já está na lista!")
    perg2 = str(input("Você quer continuar? [S/N] ")).upper()
    if perg2 == 'N':
        break
    if perg2 != 'S' and 'N':
        print("Comando Desconhecido! Tente novamente.")
print(f"Esses foram os números digitados:\n{sorted(lista)}")"""




#Treino de LISTAS: Ex080 - Lista ordenada sem repetições

"""lista = []

for no in range(0, 5):
    dig = int(input("Digite um valor: "))
    if no == 0 or dig > lista[-1]:
        lista.append(dig)
    else:
        pos = 0
        while pos < len(lista):
            if dig <= lista[pos]:
                lista.insert(pos, dig)
                break
            pos += 1
print(f"Os valores digitados em ordem foram: {lista}")"""




#Treino de LISTAS: Ex081 - Extraindo dados de uma lista

"""lista = []
cont = 0
void = ''

while True:
    perg = int(input("Digite um número: "))
    lista.append(perg)
    cont += 1
    perg2 = str(input("Deseja continuar? [S/N] ")).upper()
    if perg2 == 'N':
        break
    if perg2 != 'S' and 'N':
        print("Comando Desconhecido! Tente novamente.")
        
lista.sort(reverse=True)
print(void)
print(f"Você digitou {cont} números.")
print(f"Os valores em ordem decrescente são: {lista}")
if 5 in lista:
    print("O número 5 faz parte dessa lista!")
else:
    print("O número 5 não faz parte dessa lista...")"""




#Treino de LISTAS: Ex082 - Dividindo valores em várias listas

"""lista = []
lista2 = []
lista3 = []
void = ''

while True:
    perg = int(input("Digite um número: "))
    lista.append(perg)
    perg2 = str(input("Deseja continuar? [S/N] ")).upper()
    if perg2 == 'N':
        break
    if perg2 != 'S':
        print("Comando Desconhecido! Tente novamente.")
    if perg % 2 == 0:
        lista2.append(perg)
    if perg % 2 != 0:
        lista3.append(perg)

print(void)
print(f"A lista original é esta: {lista}")
print(void)
print(f"A lista com números pares é esta: {lista2}")
print(f"E a lista com números ímpares é esta: {lista3}")"""




#Treino de LISTAS: Ex083 - Validando expressões matemáticas

perg = str(input("Digite uma expressão: "))

lista = []

for pare in perg:
    if pare == '(':
        lista.append('(')
    elif pare == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão é inválida!")
