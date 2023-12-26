print("=" * 25)
print("    MAGAIESKI'S BANK")
print("=" * 25)

din = int(input("Qual valor voce quer sacar? "))

total = din
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f"Total de {totalced} cedula(s) de ${ced} ")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        totalced = 0

        if total == 0:
            break
