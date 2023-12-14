termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razao da PA: "))

for c in range(termo, razao * 10, razao):
    print(c, end=' --> ')

print("FIM")
