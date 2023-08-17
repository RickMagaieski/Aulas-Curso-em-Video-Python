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

"""from time import sleep

frase = input("Digite algo: ").upper().strip()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
for p in range(len(juntar)-1, -1, -1):
    inverso += juntar[p]
print(f"A frase {frase} ao contrário fica {inverso}...")
sleep(1.5)
if juntar == inverso:
    print("Portanto, a sua frase é um PALINDROMO!")
else:
    print("Portanto, a sua frase não é um PALINDROMO...")"""




#Treino de FOR: Ex054 -

"""from datetime import date

perg = int(input("Você quer colocar quantas datas? "))
hoje = date.today().year
cont1 = 0
cont2 = 0
for m in range(1, perg + 1):
    data = int(input(f"Qual é a data de nascimento da {m}° pessoa? "))
    conta = hoje - data
    if conta < 18:
        cont1 += 1
    elif conta >= 18:
        cont2 += 1
print(f"Das {perg} datas de nascimentos inseridas, {cont2} são de pessoas maiores de 18 anos e {cont1} são de menores.")
"""




#Treino de FOR: Ex055 - Maior e menor da sequência

"""perg = int(input("Digite quantos pesos serão lidos: "))
lista = []
for p in range(1, perg + 1):
    peso = float(input(f"Digite o peso da {p}° pessoa: "))
    lista.append(peso)
print(f"O maior peso foi {max(lista)}Kg e o menor foi {min(lista)}Kg")"""




#Treino de FOR: Ex056 - Analisador Completo

"""from time import sleep

perg = int(input("Digite o número de pessoas que você irá analisar: "))
soma = 0
cont = 0
veio = ''
idadeveio = 0
for pe in range(1, perg + 1):
    print(f"====== {pe}° PESSOA ======")
    pessoa = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    sexo = input("Para o masculino digite M e F para feminino: ").upper()
    soma += idade / perg
    if sexo == "F" and idade < 20:
        cont += 1
    if idade < 9999 and sexo == "M":
        veio = pessoa
        idadeveio = idade
print("Analisando informações...")
sleep(2)
print("De acordo com as informações fornecidas:")
sleep(1.8)
print("A média de idade do grupo é de {:.1f} anos".format(soma))
print(f"Existe(m) {cont} mulher(es) com menos de 20 anos.")
if veio and idadeveio:
    print(f"E o homem mais velho do grupo se chama {veio} com {idadeveio} anos de idade! ")
else:
    print("Não foi inserido dados de nenhum homem.")"""




#Treino de WHILE: Ex057 + Ex058 + Ex059 - Validação de sexo + Jogo de Advinhação + Menu de Opções

"""from time import sleep
from random import randint

print("=" * 30)
print("Seja Bem Vindo ao Esfinge V2.0")
print("=" * 30)
sleep(0.5)
print("Olá, antes de inciarmos nos forneca algumas informações!")
sleep(2)
nome = ''
esc = 0
while True:
    sexo = input('Por favor, nos informe o seu sexo\nDigite [M] para masculino e [F] para feminino: ').upper()
    esc = 0
    while True:
        if sexo == "F":
            nome = input("Qual é o seu nome minha querida? ")
        elif sexo == 'M':
            nome = input("Qual é o seu nome meu querido? ")
        else:
            print("Sexo Desconhecido")
            break
        sleep(0.5)
        if sexo == "M":
            print(f"Seja bem vindo(a) a Esfinge {nome}!")
        elif sexo == "F":
            print(f"Seja bem vinda a Esfinge {nome}!")

        void = ''
        sleep(1.5)

        while True:
            print(void)
            print("========== MENU ==========")
            print("[1] Começar o jogo\n[2] Trocar Informações\n[3] Sobre\n[4] Sair")
            esc = int(input("Sua escolha: "))
            print("=" * 26)

            if esc == 1:
                while True:
                    print(void)
                    print("Entrando na Pirâmide...")
                    sleep(1.5)
                    print("Muahahahahhah, eu sou a Esfinge! E eu tenho um desafio para você!!!!!")
                    sleep(2)
                    print("Irei escolher um número entre 1 e 10 e quero que advinhe em qual número eu pensei!")
                    sleep(1)
                    for c in range(1, 4):
                        sleep(0.8)
                        print(".", end='')
                    sleep(2)
                    print("\nAdvinhe corretamente ou eu te devorarei! Boa sorte...")
                    sleep(1.5)
                    adv = randint(1, 10)
                    cont = 0

                    while True:
                        cont += 1
                        perg = int(input('Sua resposta: '))

                        if perg != adv:

                            if cont == 1:
                                print("Foi se a primeira chance hahahaa!")
                                sleep(1.7)

                            if cont == 2:
                                print("De novo...")
                                sleep(1.7)

                            if cont == 3:
                                print("Foi se a ultima chance de sobreviver hahahaha!")
                                sleep(1.7)

                        if perg == adv and cont == 1:
                            print("Não pode ser, como acertaste de primeira?")
                            sleep(2)
                            print("GRRR...")
                            sleep(1.5)
                            print("Mereces um prêmio... tome esta espada.")
                            sleep(2.3)
                            print("Agora suma de minha frente!!")
                            sleep(1.8)
                            break

                        if perg == adv and cont != 1:
                            print("Você acertou, parabéns, sua vida será poupada...")
                            sleep(1.8)
                            print("Pode seguir, criaturinha ínfima...")
                            sleep(1.9)
                            break

                        if perg != adv and cont == 3:
                            print("Suas chances acabaram... Hahahahahaha!")
                            sleep(2.5)
                            print("!!NHAC!!")
                            sleep(2)
                            print("Você foi devorado!")
                            sleep(1.5)
                            break

                    print(void)
                    print("Gostaria de jogar de novo ou de voltar para o menu?")
                    resposta = input("Digite [J] para jogar ou [S] para sair: ").upper()
                    if resposta == "S":
                        break
            if esc == 2:
                break

            if esc == 3:
                print("Olá! Meu nome é Henrique e eu estou tentando fazer essa bagaça funcionar"
                      "a dois dias (contando hoje), então eu sinceramente espero terminar hoje!")
                menu = input("Digite [M] para retornar ao menu: ").upper()

            if esc == 4:
                break
        if esc == 4:
            break
    if esc == 4:
        print("Finalizando o programa...")
        sleep(2)
        print("-------------------")
        print("Programa finalizado")
        break"""




#Treino de WHILE : Ex060 - Cálculo de Fatorial

"""fat = int(input("Digite um número para caulcularmos o seu fatorial: "))
f = 1
print(f"{fat}! = ", end='')
while True:
    print(f"{fat}", end=' ')
    if fat > 1:
        print(f"X", end=' ')
    else:
        print(f"= {f}", end='')
        break
    f *= fat
    fat -= 1"""

#Outra Possibilidade:

"""fato = int(input("Digite um número para calcularmos o seu fatorial: "))
conta = 1
print(f"{fato}! = ", end='')
for fat in range(fato, 0, -1):
    conta *= fat
    print(f"{fat}", end='')
    if fat > 1:
        print(" X ", end='')
    else:
        print(f" = {conta}", end='')"""




#Treino de WHILE: Ex061 - Progressão Aritimética V2.0

"""termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
cont = 0
while cont < 10:
    print(f"{termo}", end=' -> ')
    termo += razao
    cont += 1
print("Fim")"""

#Outra Possibilidade:

"""termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
decimo = termo + 10 * razao
for pa in range(termo, decimo, razao):
    print(pa, end=" -> ")
print("Fim")"""




#Treino de WHILE: Ex062 - Super Progressão Aritimética V3.0

"""from time import sleep

termo = int(input("Digite o termo da progressão: "))
razao = int(input('Digite a razão da progressão: '))
cont = 0
var = 0
mais = 10
while True:
    var += mais
    while cont < var:
        print(f"{termo}", end=' -> ')
        termo += razao
        cont += 1
    print("Pausa")
    var = int(input("Quantos termos a mais você quer ver? "))
    if var == 0:
        print("Encerrando programa...")
        sleep(1.5)
        print("Programa encerrado.")
        break"""




#Treino de WHILE: Ex063 - Sequência de Fibonacci

"""perg = int(input("Digite quantos termos você deseja ver: "))
termo1 = 0
termo2 = 1
print(f"{termo1} -> {termo2} ->", end=' ')
conta = 2
while not conta == perg:
    termo3 = termo1 + termo2
    print(f"{termo3} ->", end=' ')
    termo1 = termo2
    termo2 = termo3
    conta += 1
print("FIM")"""




#Treino de WHILE: Ex064 - Tratando Vários Valores

"""from time import sleep

cont = 0
soma = 0
void = ''
while True:
    dig = int(input("Digite um número [Para parar digite 999]: "))
    if dig != 999:
        soma += dig
        cont += 1
    else:
        break
sleep(1)
print(void)
print(f"Foram digitados {cont} valores, cuja a soma total dá {soma}")"""




#Treino de WHILE: Ex065 - Maior e Menor Valores

"""cont = 0
soma = 0
lista = []

while True:
    num = int(input("Digite um número: "))
    perg = input("Você quer continuar [S/N]? ").upper()
    cont += 1
    soma += num
    lista.append(num)
    if perg == 'N':
        break
media = soma / cont
print(f"Você digitou {cont} números e a média entre eles deu {media}")
print(f"O maior valor foi {max(lista)} e o menor valor foi {min(lista)}")"""




#Treino de WHILE: Ex066 - Vários numeros com flag

"""soma = 0
cont = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        soma += num
        cont += 1
    else:
        break
print(f"Foram digitados {cont} números e a soma entre eles deu {soma}")"""




#Treino de WHILE: Ex067 - Tabuada V3.0

"""void = ''
print(void)
perg = int(input("Digite o número da tabuada que você quer ver: "))
cont = 0

print(void)

print("=" * 13)
while cont < 10:
    cont += 1
    mult = perg * cont
    print(f"{perg} X {cont} = {mult}")
print("=" * 13)"""




#Treino de WHILE: Ex068 - Jogo par ou ímpar

"""from random import randint
from time import sleep

print("=" * 30)
print("{:^30}".format("O Famoso Par ou Ímpar"))
print("=" * 30)

void = ''
pc = randint(1, 10)
cont = 0
print(void)
while True:
    esc = str(input("Par ou ímpar? ")).upper()[0]
    sleep(0.5)
    num = int(input("Escolha um número: "))
    soma = num + pc

    cont += 1
    if esc == "P" and soma % 2 == 0:
        print(f"O pc jogou o número {pc} e você o número {num}, a soma entre ambos deu {soma}")
        sleep(1)
        print("Parabéns... você venceu!")
        sleep(1.5)
        print("E eu quero tentar de novo!")
        print(void)
    if esc == "P" and soma % 2 == 1:
        print(f"O pc jogou o número {pc} e você o número {num}, a soma entre ambos deu {soma}")
        sleep(1)
        print("Você peeeeerdeeeu!")
        print(void)
        sleep(1.5)
        print(f"\033[1m[total de vitórias {cont - 1}]\033[m")
        break
    if esc == "I" and soma % 2 == 0:
        print(f"O pc jogou o número {pc} e você o número {num}, a soma entre ambos deu {soma}")
        sleep(1)
        print("Você peeeeerdeeeu!")
        print(void)
        sleep(1.5)
        print(f"\033[1m[total de vitórias {cont - 1}]\033[m")
        break
    if esc == "I" and soma % 2 == 1:
        print(f"O pc jogou o número {pc} e você o número {num}, a soma entre ambos deu {soma}")
        sleep(1)
        print("Parabéns... você venceu!")
        sleep(1.5)
        print("E eu quero tentar de novo!")
        print(void)"""




#Treino de WHILE: Ex069 - Analise de Dados do Grupo

"""from time import sleep
mais18 = 0
mume20 = 0
homens = 0
void = ''

while True:
    print("=" * 30)
    sexo = str(input("Digite o sexo da pessoa: ")).upper()[0]
    idade = int(input("Digite a idade da pessoa: "))
    print("=" * 30)
    print(void)
    perg = input("Quer continuar? [S/N] ").upper()
    print(void)
    if sexo == 'F' and idade < 20:
        mume20 += 1
    if sexo == 'M':
        homens += 1
    if idade > 18:
        mais18 += 1
    if perg == 'N':
        break
print("=" * 35)
print("\033[1mSegundo os dados, ao todo existem:\033[m")
print(void)
print(f"[{mais18}] Pessoa(s) com idade superior a 18 anos.\n[{mume20}] Mulher(es) com menos de 20 anos"
      f"\n[{homens}] Homem(ns)")"""




#Treino de WHILE: Ex070 - Estatística em Produtos

"""from time import sleep

void = proba = ''
mais1000 = soma = 0
produtos1000 = []
n = []
produtos = []

print("~" * 33)
print("{:^30}".format("LOJAS MAGAIESKI"))
print("~" * 33)

while True:
    print(void)
    print("=" * 32)
    pro = str(input("Digite o nome do produto: "))
    valor = int(input("Digite o valor do produto: "))
    print("=" * 32)
    print(void)
    perg = str(input("Deseja continuar? ")).upper()[0]

    soma += valor
    n.append(valor)
    if valor > 1000:
        produtos.append(pro)

    if valor > 1000:
        mais1000 += 1
        produtos1000.append(pro)
    if valor == min(n):
        proba = pro

    if perg == 'N':
        break

print(void)
print(void)
print("=" * 30)
print(f"O gasto total na compra foi de R${soma}")
print(f"O produto mais barato foi {proba} que custa R${min(n)}")
print(f"{mais1000} Produtos custam mais de R$1000:")
print(f"{produtos}")
print("=" * 30)
sleep(3)
print("Volte Sempre!")"""




#Treino de WHILE: Ex071 - Simulador de Caixa Eletrônico

"""from time import sleep

void = ''

print("=" * 30 )
print("{:^30}".format("MAGAIESKI'S BANK"))
print("=" * 30)

print(void)


saque = int(input('Digite o valor que você deseja sacar: '))

n50 = n20 = n10 = n1 = 0

while True:
    if saque >= 50:
        saque -= 50
        n50 += 1
    elif saque >= 20:
        saque -= 20
        n20 += 1
    elif saque >= 10:
        saque -= 10
        n10 += 1
    elif saque >= 1:
        saque -= 1
        n1 += 1
    if saque == 0:
        break
print(void)
print("-" * 35)
print("Foi Sacado:")
print(void)
print(f"{n50} nota(s) de R$50\n{n20} nota(s) de R$20\n{n10} nota(s) de R$10\n{n1} nota(s) de R$1")
print("-" * 35)"""







