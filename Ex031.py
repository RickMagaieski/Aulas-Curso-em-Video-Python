import emoji
kms = float(input("Qual será a distância da viagem? "))
calculo1 = 0.50 * kms
calculo2 = 0.45 * kms
if kms <= 200:
    print("Para {:.1f}Km o valor será de R${:.2f}.".format(kms, calculo1))
else:
    print("Para {:.1f}Km o valor será menor, sairá por R${:.2f}.".format(kms, calculo2))
print("Faça uma boa viagem 😊!")
