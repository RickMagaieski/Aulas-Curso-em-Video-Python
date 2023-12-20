print()

termo = int(input("Primeiro Termo: "))
razao = int(input("Razao da PA: "))

cont = 1
n = 10

print()

while True:

    while cont <= n:
        print(f"{termo} -> ", end="")

        termo += razao
        cont += 1
    print("PAUSA", end="")

    perg = int(input("\nQuantos termos a mais voce quer ver? "))
    n += perg

    if perg == 0:
        break

print()

print(f"Progressao finalizada com {cont - 1} termos mostrados.")
