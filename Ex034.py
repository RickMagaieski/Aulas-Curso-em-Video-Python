sal = float(input("Digite o salário atual do funcinário: R$"))
sal1 = sal * 10 / 100 + sal
sal2 = sal * 15 / 100 + sal
if sal > 1250:
    print("O aumento foi de 10% para este funcionário, que antes recebia R${:.2f} e agora receberá R${:.2f}.".format(sal, sal1))
if sal <= 1250:
    print("O aumento foi de 15% para este funcionário, que antes recebia R${:.2f} e agora receberá R${:.2f}.".format(sal, sal2))
