pt = int(input("Primeiro termo: "))
ra = int(input("Razao da PA: "))

cont = 1

while cont <= 10:
    print(f"{pt} ->", end=' ')
    pt += ra
    cont += 1

print("Fim")
