#Treino de TUPLA: Ex072 - Números por Extenso
"""
numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
                 "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

while True:
    digito = int(input("Digite um número entre 0 e 20: "))
    cont = 0

    for contagem in range(len(numeros)):
        if contagem == digito:
            print(f"Você digitou o número \033[1m{numeros[contagem]}\033[m")
            cont += 1
            break
    if digito > len(numeros) - 1 or digito < 0:
        print("Tente novamente! Número fora do permitido.")
    if cont > 0:
        break"""




#Treino de TUPLA: Ex073 - Tuplas com Universidades

"""
void = ''
uni = ("Harvard", "MIT", "Stanford", "UC Berkeley", "Caltech", "Oxford", "Cambridge", "Chicago",
       "Imperial College London", "ETH Zurich", "UPenn", "Yale", "Princeton", "Cornell", "UCLA", "UC San Diego",
       "Columbia", "UW", "Edinburgh", "Tokyo")

print(void)

print(f"\033[1m# As primeiras 5 melhores universidades são:\033[m")
print(void)
for cinco in uni[0:5]:
    print("\033[1m*\033[m", cinco)

print(void)

print(f"\033[1m# As ultímas 4 melhores universidades são \033[m:")
print(void)
for cinco in uni[-4:]:
    print("\033[1m*\033[m", cinco)

print(void)

print(f"\033[1m# Universidades em ordem alfabética:\033[m")
print(void)
for cinco in sorted(uni):
    print("\033[1m*\033[m", cinco)

print(void)

for local, univer in enumerate(uni):
    if 'Yale' in univer:
        print(f"\033[1m# A universidade de {univer} está na {local + 1}ª posição\033[m")"""




#Treino de TUPLAS: Ex074 - Maior e menor valores em Tupla
"""
from random import randint

void = ''
lista = []

for numeros in range(0, 5):
    lista.append(randint(0, 10))

tupla = tuple(lista)

print("Os números gerados foram:", end=' ')
for tup in tupla:
    print(tup, end=' ')

print(f"\nO maior valor gerado foi o valor {max(tupla)}")
print(f"O menor valor gerado foi o valor {min(tupla)}")"""




#Treino de TUPLAS: Ex075 - Análise de dados em uma Tupla

"""void = ''
lista = []
lista2 = []
cont = 0
cont3 = 0

for num in range(0, 4):
    digi = (int(input("Digite um número: ")))
    lista.append(digi)
    if digi == 9:
        cont += 1
    if digi % 2 == 0:
        lista2.append(digi)
    if digi == 3:
        cont3 += 1

numeros = tuple(lista)
par = tuple(lista2)

print(void)

print(f"Você digitou os seguintes valores: {numeros}")

print(void)

if cont3 == 1:
    print(f"O número 3 apareceu na posição {numeros.index(3)}.")
elif 3 not in numeros:
    print("O número 3 não foi encontrado.")
if cont3 > 1 and 3 in numeros[0:2]:
    print(f"O número 3 apareceu nas seguintes posições: {numeros.index(3)}, {numeros.index(3, 2)}")
elif cont3 > 1 and 3 in numeros[0:3]:
    print(f"O número 3 apareceu nas seguintes posições: {numeros.index(3)}, {numeros.index(3, 2) + 1}")

print(f"O valor 9 apareceu {cont} vez(es).")

print("Esses são os números pares digitados:", end=' ')
for pares in par:
    print(pares, end=' ')"""




#Treino de TUPLAS: Ex076 - Lista de Preços com Tupla
"""
void = ''
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 33.90)

print("\033[1m=" * 51)
print(f"{'MAGAIESKIS SHOP':>32}\033[m")
print("\033[1m=\033[m" * 51)

for pro in range(0, len(produtos)):
    if pro % 2 == 0:
        print(f"\033[1m*\033[m {produtos[pro]:.<40}R$", end=' ')
    else:
        print(f"{produtos[pro]:>6.2f}")"""




#Treino de TUPLAS: Ex077 - Contando vogais em Tupla
"""
palavras = ('MESA', 'CADEIRA', 'JANELA', 'CELULAR', 'COMPUTADOR', 'GELADEIRA', 'CAMA', 'ESCRIVANINHA', 'TAPETE')

for c in palavras:
    print(f"\nPara a palavra {c} nos temos:", end=' ')
    for vogais in c:
        if vogais in 'AEIOU':
            print(vogais, end=' ')"""




#Treino de LISTAS: Ex078 - Maior e Menor Valores na Lista
"""
void = ''
lista = []
posma = []
posme = []

for n in range(0, 5):
    lista.append(int(input(f"Digite um número para a posição {n}: ")))

for n, p in enumerate(lista):
    if max(lista) == p:
        posma.append(n)
    if min(lista) == p:
        posme.append(n)

print(void)
print(f"Sua lista: {lista}")
print(void)

if len(posma) == 1:
    print(f"\nO maior número da sua lista foi o número {max(lista)} que está na posição:", end=' ') #Maior no singular
    for c in posma:
        print(f"{c}...")
else:
    print(f"\nO maior número da sua lista foi o número {max(lista)} que está nas posições:", end=' ') #Maior no plural
    for con in posma:
        print(f"{con}...", end=' ')


if len(posme) == 1:
    print(f"\nO menor número da sua lista foi o número {min(lista)} que está na posição:", end=' ') #Menor no singular
    for co in posme:
        print(f"{co}...", end=' ')
else:
    print(f"\nO menor número da sua lista foi o número {min(lista)} que está nas posições:", end=' ') #Maior no plural
    for cont in posme:
        print(f"{cont}...", end=' ')

print(void)"""




#Treino de LISTAS : Ex079 - Valores Únicos em Uma Lista
"""
from time import sleep
lista = []
cont = 1
void = ''

print(void)
print("Números repetidos não serão adicionados!")
sleep(2)
print(void)

while True:
    n = int(input("Digite um número: "))

    if n not in lista:
        lista.append(n)
    else:
        print(void)
        print("O valor não foi adicionado.")
        print(void)

    perg = str(input("Deseja continuar? [S/N] ")).upper()

    if perg != 'S' and perg != 'N':
        print("Comando Inválido, tente novamente!")
        break
    elif perg == 'N':
        break

lista.sort()
print(void)
print(f"Sua lista já ordenada: {lista}")"""




#Treino de LISTAS: Ex080 - Lista Ordenada Sem Repetições

