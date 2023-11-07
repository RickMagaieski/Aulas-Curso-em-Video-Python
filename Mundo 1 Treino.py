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




#Treino de IF: Ex029 - Radar Eletrônico
"""
from time import sleep

vel = float(input("Qual foi a velocidade do carro? "))

print()

if vel > 80:
    print(f"\033[1m\033[31m{vel}Km/h\033[m")
    sleep(1)
    print()
    print(f"\033[1mVocê ultrapassou o limite de velocidade! Você terá que pagar ${(vel - 80) * 7} de multa\033[m")
else:
    print(f"\033[1m\033[32m{vel}Km/h\033[m")
    sleep(1)
    print()
    print("\033[1mVocê está dentro do limite de velocidade. Tenha um ótimo dia :)\033[m")"""




#Treino de IF: Ex030 - Par ou Ímpar?
"""
print()

num = int(input("Digite um número qualquer: "))

if num % 2 == 0:
    print(f"\033[1mO número \033[1m\033[32m{num}\033[m\033[1m é um número par!\033[m")
else:
    print(f"\033[1mO número \033[1m\033[36m{num}\033[m\033[1m é um número ímpar!\033[m")"""




#Treino de IF: Ex031 - Custo da Viagem
"""
pas = float(input("Digite a distância do seu destino: "))

if pas <= 200:
    print(f"Para uma viagem de {pas}Km, sua passagem custará ${pas * 0.20:.2f}")
elif pas > 200:
    print(f"Para uma viagem de {pas}Km, sua passagem custará ${pas * 0.135:.2f}")"""




#Treino de IF: Ex032 - Ano Bissexto
"""
from time import sleep
from datetime import date
from time import sleep

print()

print("Digite 0 para analisar esse ano!")
sleep(1)

print()

ano = int(input("Que ano deseja analisar?"))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é um ano BISSEXTO!")
else:
    print(f"O ano de {ano} não é um ano BISSEXTO...")"""




#Treino de IF: Ex033 - Maior e Menor Valores
"""
print()

p1 = int(input("Primeiro número: "))
p2 = int(input("Segundo número: "))
p3 = int(input("Terceiro número: "))

print()

if p1 > p2 and p1 > p3:
    print(f"O número {p1} é o maior número!")
if p2 > p1 and p2 > p3:
    print(f"O número {p2} é o maior número!")
if p3 > p1 and p3 > p2:
    print(f"O número {p3} é o maior número!")

if p1 < p2 and p1 < p3:
    print(f"O número {p1} é o menor número!")
if p2 < p1 and p2 < p3:
    print(f"O número {p2} é o menor número!")
if p3 < p1 and p3 < p2:
    print(f"O número {p3} é o menor número!")"""




#Treino de IF: Ex034 - Aumentos múltiplos
"""
print()

sal = float(input("Digite o salário do funcionário: "))

if sal > 1250:
    print(f"O salário do funcionário que antes era de ${sal:.2f} agora será ${sal * 10 / 100 + sal:.2f}")
else:
    print(f"O salário do funcionário que antes era de ${sal:.2f} agora será ${sal * 15 / 100 + sal:.2f}")"""




#Treino de IF: Ex035 - Analisando Triângulos v1.0
"""
print()

ps1 = float(input("Primeiro Segmento: "))
ss2 = float(input("Segundo Segmento: "))
ts3 = float(input("Terceiro Segmento: "))

print()

if ps1 < ss2 + ts3 and ss2 < ps1 + ts3 and ts3 < ss2 + ps1:
    print("Esses valores podem formar um triângulo!")
else:
    print("Esses valores não podem formar um triângulo...")"""
