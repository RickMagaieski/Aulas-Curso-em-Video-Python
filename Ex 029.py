print("=="*8)
print("RADAR DA BR 106")
print("=="*8)
per = int(input("Qual foi a velocidade do carro? "))
multa = float(per - 80) * 7
if per <= 80:
    print(f"A velocidade de {per}Km/h é adequada. Tenha um boa viagem!")
else:
    print("MULTA! Por excesso de velocidade.\nO valor a ser pago será de R${:.2f}.".format(multa))
print("A PRF agradeçe sua compreensão.")
