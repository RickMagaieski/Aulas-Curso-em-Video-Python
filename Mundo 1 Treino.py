#Treino de STRINGS: Ex022 - Analisador de Textos
"""
from time import sleep

nome = str(input("Digite o seu nome completo: ")).strip()

print()

print("Analisando seu nome...")
sleep(1)
separado = nome.split()

print()

print(f"O seu nome em letras maiúsculas é \033[1m{nome.upper()}\033[m")
print(f"O seu nome em letras minúsculas é \033[1m{nome.lower()}\033[m")
print(f"O seu nome tem no total {len(''.join(separado))} letras")
print(f"O seu primeiro nome que é \033[1m{separado[0]}\033[m tem {len(separado[0])} letras")"""




#Treino de STRINGS: Ex023 - Separando dígitos de um número
"""
n = int(input("Digite um numero: "))

print()

print(f"Analisando o número {n}")

print()

un = n // 1 % 10
de = n // 10 % 10
ce = n // 100 % 10
mi = n // 1000 % 10

print(f"Unidade: {un}")
print(f"Dezena: {de}")
print(f"Centena: {ce}")
print(f"Milhar: {mi}")"""




#Treino de STRINGS: Ex024 - Verificando as primeiras letras de um texto
"""
cidade = str(input("Digite o nome de uma cidade: ")).upper()

print(cidade[:5] == 'SANTO')"""




#Treino de STRINGS: Ex025 - Procurando uma string dentro de outra
"""
print()

nome = str(input("Digite seu nome completo: ")).upper()

print(f"Seu nome contém Silva? {'SILVA' in nome}")"""




#Treino de STRING: Ex026 - Primeira e última ocorrência de uma string
"""
print()

pa = str(input("Digite uma frase: ")).lower().strip()

print()

print(f"A letra A aparece {pa.count('a')} vezes")
print(f"A primeira letra A aparece na posição {pa.find('a')}")
print(f"A última letra A aparece na psição {pa.rfind('a')}")"""




#Treino de STRING: Ex027 - Primeiro e último nome de uma pessoa
"""
print()

nome = str(input("Digite seu nome completo: "))

print()

separado = nome.split()

print(f"Seu primero nome é {separado[0]}\nE seu último nome é {separado[-1]}")"""




#Treino de IF: Ex028 - Jogo da Adivinhação v.1.0
"""
from random import randint
from time import sleep

print("=" * 29)
print(f"{'JOGO DE ADVINHAÇÃO':>23}")
print("=" * 29)

print()

print("Tente advinhar o número em que estou pensando...")
sleep(0.8)
perg = str(input("Em qual número pensei? "))

print("PROCESSANDO...")
sleep(1)
print()

if perg == randint(0, 5):
    print("Acertou!! Parabéns :)")
else:
    print("Errou... tente de novo!")"""
