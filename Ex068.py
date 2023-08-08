from random import randint
from time import sleep

valor = randint(0, 10)
cont = 0
void = ''

while True:

    print(void)
    perg = str(input("Par ou ímpar [I/P]? ")).upper().strip()
    num = int(input("Joga um valor: "))

    print(void)

    soma = num + valor
    par = soma % 2 == 0
    impar = soma % 2 != 0

    print(f"Você jogou {num} e o computador jogou {valor}. ", end='')


    if perg == 'P' and par:
        cont += 1
        print(f"A soma de ambos os números deu {soma} que é PAR")
        sleep(0.8)
        print("Você venceu! Parabéns mí amigo...")
        sleep(0.8)
        print("Vamos jogar de novo!")

    if perg == 'I' and impar:
        cont += 1
        print(f"A soma de ambos os números deu {soma} que é ÍMPAR")
        sleep(0.8)
        print("Você venceu! Parabéns mí amigo...")
        sleep(0.8)
        print("Vamos jogar de novo!")

    if perg == 'I' and par:
        cont += 1
        print(f"A soma de ambos os números deu {soma} que é PAR")
        sleep(0.8)
        print("Você perdeu ! Hahahaha...")
        sleep(0.8)
        print(f"Você venceu {cont - 1} vez(es)")
        sleep(1.5)
        print("GAME OVER!")
        break

    if perg == 'P' and impar:
        cont += 1
        print(f"A soma de ambos os números deu {soma} que é ÍMPAR")
        sleep(0.8)
        print("Você perdeu ! Hahahaha...")
        sleep(0.8)
        print(f"Você venceu {cont - 1} vez(es)")
        sleep(1.5)
        print("GAME OVER!")
        break
