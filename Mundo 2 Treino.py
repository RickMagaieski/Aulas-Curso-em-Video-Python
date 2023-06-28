#Treino de FOR: Ex047

from time import sleep
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
                print("O valor excedeu o valor original apenas por toc do Dev ;)")
