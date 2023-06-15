from time import sleep
print("========== LOJAS MAGAIESKI'S ==========")
gast = float(input("Qual foi o valor total das compras? R$"))
print("MÉTODOS DE PAGAMENTO")
print("[ 1 ] Á vista dinheiro\n[ 2 ] Á vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão ")
esc = int(input("Qual será a opção escolhida? "))
if esc == 1:
    print("Analisando...")
    sleep(1)
    cont = gast - ((gast * 10) / 100)
    print("Por ser um pagamento á vista e em dinheiro, você obterá 10% de desconto!")
    sleep(0.5)
    print("Sua compra saiu de R${:.2f}, pelo valor de R${:.2f}".format(gast, cont))
elif esc == 2:
    print("Analisando...")
    sleep(1)
    cont = gast - ((gast * 5) / 100)
    print("Por ser um pagamento á vista e no cartão, você obterá 5% de desconto!")
    sleep(0.5)
    print("Sua compra saiu de R${:.2f}, por R${:.2f}".format(gast, cont))
elif esc == 3:
    print("Analisando...")
    sleep(1)
    cont = gast / 2
    sleep(0.5)
    print("Sua compra de R${:.2f} foi parcelada em 2x de R${:.2f} sem juros.".format(gast, cont))
elif esc == 4:
    par = int(input("Em quantas parcelas? "))
    sleep(1)
    conta = gast + (gast * 20 / 100)
    parcelas = conta / par
    print("Analisando...")
    print("Sua compra será parcelada em {}x de R${:.2f} com juros.".format(par, parcelas))
    sleep(0.5)
    print("A sua compra de R${:.2f}, ficará no final pelo valor de R${:.2f}".format(gast, conta))
else:
    print("Comando desconhecido")
