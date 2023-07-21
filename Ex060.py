#Conta de fatorial usando o loop While:

n = int(input("Digite um número para calcularmos seu fatorial: "))
c = n
f = 1
print(f"{n}! = ", end='')
while c > 0:
    print(f"{c}", end=' ')
    if c > 1:
        print("X", end=' ')
    else:
        print(f"= {f}", end=' ')
    f *= c
    c -= 1

#Cálculo de fatorial com loop For:

n = int(input("Digite um número para calcularmos seu fatorial: "))
f = 1
print(f"{n}! =", end=' ')
for fat in range(n, 0, -1):
    print(f"{fat}", end=' ')
    if fat > 1:
        print("X", end=' ')
    else:
        print("=", end=' ')
    f *= fat
print(f"{f}", end=' ')
