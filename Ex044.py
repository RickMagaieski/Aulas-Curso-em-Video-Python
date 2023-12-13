print("========== MAGAIESKI'S SHOP ==========")

valor = float(input('Total da Compra: $'))

print("[ 1 ] A vista dinheiro/cheque\n[ 2 ] A vista no cartao\n[ 3 ] 2X no cartao\n[ 4 ] 3x ou mais no cartao")

print()

op = int(input("Digite o numero da sua opcao: "))

if op == 1:
    print(f"A compra que custava ${valor:.2f}, a vista, saira por ${valor - valor * 10 / 100:.2f}")
elif op == 2:
    print(f"A compra que custava ${valor:.2f}, no cartao, saira por ${valor - valor * 5 / 100:.2f}")
elif op == 3:
    print(f"O total foi de ${valor:.2f}")
elif op == 4:
    par = int(input("Quantas parcelas? "))

    juros = valor * 20 / 100 + valor

    print()

    print(f"Sua compra sera parcelada em {par}X de ${juros/par:.2f} com juros.")
    print(f"Sua compra de $ {valor:.2f} ira custar ${juros:.2f} no final.")
