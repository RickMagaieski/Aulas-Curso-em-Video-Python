print()

dis = float(input("Digite a distância da sua viagem: "))

if dis > 200:
    print(f"A sua viagem de {dis:.2f}Km irá te custar um total de ${dis * 0.45:.2f}")
elif dis < 200:
    print(f"A sua viagem de {dis:.2f}Km irá te custar um total de ${dis * 0.50:.2f}")
