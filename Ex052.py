print()

n = int(input("Digite um numero: "))

cont = 0

print()

for p in range(1, n + 1):
    if n % p == 0:
        print(f"\033[1;32m{p}\033[m", end=' ')
        cont += 1
    else:
        print(f"\033[1;31m{p}\033[m", end=' ')

print()

print(f"\nO numero {n} foi divisivel {cont} vez(es)")

if cont > 2:
    print("Por isso esse numero nao e um numero primo.")
else:
    print("Por isso esse numero e um numero primo!")
