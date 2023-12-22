print()

print("Se voce quiser encerrar o programa, digite 999")

print()

cont = 0
n = 0
som = 0

while n != 999:

    n = int(input("Digite um numero: "))

    if n != 999:
        cont += 1
        som += n

print(f"Foram digitados {cont} e a soma entre eles foi de {som}")
