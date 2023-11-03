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




