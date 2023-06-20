termo = int(input("Primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = termo + 10 * razao
for pa in range(termo, decimo, razao):
    print(pa,  end=' --> ')
print(end="FIM")
