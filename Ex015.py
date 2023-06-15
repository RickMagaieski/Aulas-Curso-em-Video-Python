k = float(input("Qual foi a quilometragem percorrida com esse carro?  "))
d = float(input("Quantos dias esse carro ficou com você? "))
print("O total que você deverá pagar pelo aluguel e pela quilometragem será de R${:.2f}".format(k*0.15 + d*60))
