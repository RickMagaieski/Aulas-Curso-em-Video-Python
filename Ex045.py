from random import randint
from time import sleep

print()

print("Suas Opcoes:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA")

print()

jog = int(input("Sua jogada: "))

print()

pc = randint(0, 2)

print("PEDRA")
sleep(0.5)
print("PAPEL")
sleep(0.5)
print("TESOOUU")
sleep(0.5)
print("RA!!")
sleep(0.5)

print()

if pc == 0 and jog == 0:
    print("Voce jogou PEDRA\nE o pc jogou PEDRA")

    print()

    print("Empate!")

elif pc == 1 and jog == 1:
    print("Voce jogou PAPEL\nE o pc jogou PAPEL")

    print()

    print("Empate!")

elif pc == 2 and jog == 2:
    print("Voce jogou TESOURA\nE o pc jogou TESOURA")

    print()

    print("Empate!")

elif jog == 0 and pc == 2:
    print("Voce jogou PEDRA\nE o pc jogou TESOURA")

    print()

    print("Voce ganhou!!!")

elif jog == 2 and pc == 0:
    print("Voce jogou TESOURA\nE o pc jogou PEDRA")

    print()

    print("Voce perdeu...")

elif jog == 1 and pc == 2:
    print("Voce jogou PAPEL\nE o pc jogou TESOURA")

    print()

    print("Voce perdeu...")

elif jog == 2 and pc == 1:
    print("Voce jogou TESOURA\nE o pc jogou PAPEL")

    print()

    print("Voce ganhou!!")

elif jog == 0 and pc == 1:
    print("Voce jogou PEDRA\nE o pc jogou PAPEL")

    print()

    print("Voce perdeu...")

elif jog == 1 and pc == 0:
    print("Voce jogou PAPEL\nE o pc jogou PEDRA")

    print()

    print("Voce ganhou!!!")
