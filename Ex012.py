p = float(input("Qual é o preço do produto? R$"))
print("O produto que antes custava R${:.2f} com 5% de desconto agora custa R${:.2f}!".format(p, (p-p*5/100)))
