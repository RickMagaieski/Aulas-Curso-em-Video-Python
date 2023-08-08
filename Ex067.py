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
        conta = num * cont
        print(f"{num} X {cont} = {conta}")
    print("=" * 13)
    print(void)
    perg = int(input("\033[4m\033[1m[Digite -1 para fechar]\033[m\033[m | Você quer ver outra tabuada? "))
    cont = 0
    if perg == -1:
        print("Fechando programa...")
        sleep(1)
        print("Volte sempre")
        break