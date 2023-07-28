#Cálculo de PA com loop WHILE:

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
cont = 0
while cont < 10:
    print(f"{termo}", end=' --> ')
    cont += 1
    termo += razao
print("Fim")



#Cálculo de PA com o loop FOR:

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = termo + 10 * razao
for pa in range(termo, decimo, razao):
    print(f"{pa}", end=' --> ')
print("Fim")
