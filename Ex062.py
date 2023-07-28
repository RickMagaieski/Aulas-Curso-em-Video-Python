from time import sleep

print("="*15)
print("Gerador de PA")
print("="*15)
while True:
    termo = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão da PA: "))
    cont = 0
    total = 10
    perg = 1
    while True:
        while cont < total:
            print(f"{termo}", end=' --> ')
            termo += razao
            cont += 1
        print("PAUSA")
        sleep(1.5)
        perg = int(input("Digite [0] para não continuar, [1] para continuar e [2] para novos valores"
                         "\nO que você quer fazer? "))
        if perg == 1:
            termo2 = int(input("Quantos termos a mais você quer ver? "))
            total += termo2
            sleep(1)
        if perg == 2:
            break
        if perg == 0:
            sleep(0.8)
            print(f"O programa encerrou com {cont} termos sendo mostrados.")
            perg += perg
            break
    if perg == 0:
        break
