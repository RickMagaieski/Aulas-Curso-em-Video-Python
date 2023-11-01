n = int(input("Digite um número: "))

n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10

print(f"Unidade: {n1}")
print(f"Dezena: {n2}")
print(f"Centena: {n3}")
print(f"Milhar: {n4}")
