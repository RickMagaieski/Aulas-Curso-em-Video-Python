sal = float(input("Digite o salário do funcionário: "))

print()

if sal >= 1250:
    print(f"O funcionário que ganhava ${sal:.2f} agora receberá ${sal * 10 / 100 + sal:.2f}")
elif sal <= 1250:
    print(f"O funcionário que ganhava ${sal:.2f} agora receberá ${sal * 15 / 100 + sal:.2f}")
