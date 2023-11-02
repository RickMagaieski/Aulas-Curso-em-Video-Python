n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo Valor: "))
n3 = int(input("Terceiro Valor: "))

print()

if n1 > n2 and n1 > n3:
    print(f"O maior valor é o valor {n1}")
if n2 > n1 and n2 > n3:
    print(f"O maior valor é o valor {n2}")
if n3 > n1 and n3 > n2:
    print(f"O maior valor é o valor {n3}")

if n1 < n2 and n1 < n3:
    print(f"O menor valor é o valor {n1}")
if n2 < n1 and n2 < n3:
    print(f"O menor valor é o valor {n2}")
if n3 < n1 and n3 < n2:
    print(f"O menor valor é o valor {n3}")
