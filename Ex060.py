"""
#Com WHILE:

numero = int(input("Digite um numero para\ncalcular seu fatorial: "))

n = 1

print(f"{numero}! =", end=' ')

while numero != 0:
    if numero > 1:
        print(f"{numero} X ", end='')
    else:
        print(f"1 = {n}", end='')

    n *= numero
    numero -= 1"""


#Com FOR:


num = int(input("Digite um numero para\ncalcular seu fatorial: "))

n = 1

print(f"{num}! = ", end="")

for fat in range(num, 0, -1):
    if fat > 1:
        print(f"{fat} X ", end="")
    else:
        print("1 = ", end="")
    n *= fat

print(n, end=" ")
