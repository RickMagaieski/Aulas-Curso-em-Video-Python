from time import sleep

void = ''
print("=" * 59)
print("---------- Seja bem vindo a sua tabuada virtual! ----------")
print("=" * 59)
sleep(0.5)

print(void)
cont = 0
perg = 'S'
while True:
    num = int(input("Digite o número da tabuada que você quer ver: "))
    print(void)
    print("=" * 13)
    while cont < 10:
        cont += 1
        print(f"{num} X {cont} = {num * cont}")
    print("=" * 13)
    print(void)
    print("\033[1m[Digite um número positivo para continuar ou um negativo para fechar]\033[m ")
    perg = int(input("Você quer continuar ? "))
    cont = 0
    if perg == -1:
        print("Fechando o programa...")
        sleep(1)
        print("Programa encerrado!")
        break
