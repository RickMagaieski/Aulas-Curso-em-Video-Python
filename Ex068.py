from random import randint

print("-=" * 20)
print(f"       VAMOS JOGAR PAR OU IMPAR!")
print("-=" * 20)

cont = 0

while True:
    pc = randint(1, 10)

    print()

    eu = int(input("Sua jogada: "))
    esc = str(input("Par ou impar? [P/I] ")).upper()

    print()

    if (eu + pc) % 2 == 0 and esc == 'P':
        print(f"Voce jogou {eu} e o computador jogou {pc}. O total deu {eu + pc} que e PAR! ")

        print()
        cont += 1

        print("Voce VENCEU!")
        print("Vamos jogar novamente...")
    if (eu + pc) % 2 != 0 and esc == 'I':
        print(f"Voce jogou {eu} e o computador jogou {pc}. O total deu {eu + pc} que e IMPAR!")

        print()
        cont += 1

        print("Voce VENCEU!")
        print("Vamos jogar novamente...")

    if (eu + pc) % 2 != 0 and esc == 'P':
        print(f"Voce jogou {eu} e o computador jogou {pc}. O total deu {eu + pc} que e IMPAR!")

        print()

        print("Voce PERDEU!")
        break
    if (eu + pc) % 2 == 0 and esc == 'I':
        print(f"Voce jogou {eu} e o computador jogou {pc}. O total deu {eu + pc} que e PAR!")

        print()

        print("Voce PERDEU!")
        break

print(f"GAME OVER. Voce venceu {cont} vez(es)")
