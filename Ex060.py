from time import sleep

print()

a = 1
n = int(input("Digite um numero: "))

while n > 0:

    print(f"{n}", end='')
    print(f" X " if n > 1 else ' = ', end='')
    a *= n
    n -= 1

print(a, end=' ')
