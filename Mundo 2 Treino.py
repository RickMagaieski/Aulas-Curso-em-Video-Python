#Treino de FOR: Ex047 - Contagem de Pares

"""from time import sleep
usuario = int(input("Digite o valor desejado para fazer a contagem: "))
perg = int(input("Digite [2] para par e [1] para ímpar: "))
sleep(1)
void = ''
if perg == 2:
    print(f"O programa irá contar os números pares de 1 até {usuario}")
    for c in range(2, usuario + 1):
        if c % 2 == 0:
            print(c, end=' ')
else:
    print(f"O programa irá contar os números ímpares de 1 até {usuario}")
    for c in range(1, usuario + 2):
        if c % 2 != 0:
            print( c, end=' ')
            if c > usuario:
                print(void)
                sleep(0.5)
                print("O valor excedeu o valor original por conta do toc do Dev ;)")"""



#Treino de FOR: Ex048 - Números ímpares multiplos de 3

"""valor = int(input("Digite o valor desejado: "))
escolha = input("A contagem seguirá ímpar ou par? ")
acu = 0
cont = 0
if escolha == "impar":
    for c in range(1, valor + 1, 2):
        if c % 3 == 0:
            cont += 1
            acu += c

elif escolha == "par":
    for c in range(1, valor + 1):
        if c % 2 == 0:
            if c % 3 == 0:
                cont += 1
                acu += c
else:
    print("Comando Desconhecido!")
print(f"A soma de todos os {cont} valores foi de {acu}")"""



#Treino de FOR: Ex049 - Tabuada

"""numero = int(input("\033[1m\033[4mDigite o número da tabuada desejada:\033[m "))
for t in range(1, 11):
    mult = t * numero
    print(f"\033[1;36m{numero} X {t}:\033[m\033[1m {mult}\033[m")"""



#Treino de FOR: Ex050 - Soma de Pares

"""from time import sleep

cont = 0
soma = 0
impares = []
for p in range(1, 7):
    num = int(input(f"Digite o {p}° valor: "))
    if num % 2 == 0:
        soma += num
    if num % 2 != 0:
        cont += 1
        impares.append(num)
print("Apenas os valores pares foram somados")
sleep(1)
print(f"A soma dos valores pares deu {soma}")
sleep(2)
print(f"Foram desconsiderados {cont} valores, os quais foram listados abaixo:\n{impares}")"""



#Treino de FOR: Ex051 - PA

"""termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
conta = termo + 10 * razao
for pa in range(termo, conta, razao):
    print("\033[7m", pa,"\033[m", end='\033[1m --> ')
print("ACABOU!")"""



#Treino de FOR: Ex052 - Números Primos

"""from time import sleep

num = int(input("Digite um número: "))
cont = 0
void = ''
for p in range(1, num + 1):
    if num % p == 0:
        print("\033[1;31m", p, "\033[m", end=" ")
        cont += 1
    else:
        print("\033[1m", p,"\033[m", end='')
print(void)
print(f"\033[1mO número\033[m\033[1;31m {num}\033[m\033[1m foi divisivel \033[m\033[1;31m{cont}\033[m\033[1m vezes!\033[m")
sleep(1)
if cont == 2:
    print(f"\033[1mPortanto o número\033[m\033[1;31m {num}\033[m\033[1m é PRIMO!\033[m")
else:
    print(f"\033[1mPortanto o número\033[m\033[1;31m {num}\033[m\033[1m não é PRIMO...\033[m")"""


#Treino de FOR: Ex053  - Detector de Palíndromos

