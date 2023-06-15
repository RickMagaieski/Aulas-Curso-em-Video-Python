print("Bem vindo ao seu conversor de moedas!")
reais = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = reais/5.13
euro = reais/5.42
dolarc = reais/3.73
print("Com R${} você poderá comprar:\nDólares|${:.2f}\nEuros|€{:.2f}\nDolares Canadenses|C${:.2f}."
      .format(reais, dolar, euro, dolarc))
