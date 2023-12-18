from random import randint
from time import sleep

cont = 0
ran = randint(1, 10)

print()

print("Sou seu PC e pensei em um numero entre 0 e 10, voce consegue adivinhar?")

sleep(2)
print()

while True:

    cont += 1

    pal = int(input("Tente a sua sorte meu caro: "))

    print()

    if ran > pal:
        print("\033[1;31mErrou, tente um valor mais alto!\033[m")
    elif ran < pal:
        print("\033[1;31mErrou, tente um valor mais baixo!\033[m")
    else:
        print(f"\033[1;32mParabens!! Voce acertou depois de {cont} tentativas!\033[m")
        break
    print()
