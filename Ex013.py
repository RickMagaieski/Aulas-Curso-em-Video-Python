s = float(input("Digite o seu salário atual: R$"))
print("Com o aumento de 15% concedido, o seu salário que antes era de R${:.2f} passará a ser R${:.2f}"
      .format(s, (s+s*15/100)))
