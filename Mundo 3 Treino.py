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

void = ''
propre = ('Cabo de força', 25.00,
         'Mouse', 30.00 ,
         'Teclado', 35.00,
         'Monitor', 520.50)

print(void)
print("=" * 40)

for c in range(0, len(propre)):
    if c % 2 == 0:
        print(f"{propre[c]:.<30}R$", end=' ')
    else:
        print(f"{propre[c]:>6.2f}")

print("=" * 40)
