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
print(f"O menor valor gerado foi o valor {min(tupla)}")
