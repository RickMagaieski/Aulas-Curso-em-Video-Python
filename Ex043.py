from time import sleep
print("Cálculo de IMC")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))
calculo = peso / (altura ** 2)
print("Calculando...")
sleep(2)
print("...")
sleep(1)
if calculo < 18.5:
    print("O valor de seu IMC foi de {:.2f}\nVocê está abaixo do peso.".format(calculo))
elif calculo < 25:
    print("O valor do seu IMC foi de {:.2f}\nVocê está no peso ideal.".format(calculo))
elif calculo < 30:
    print("O valor do seu IMC foi de {:.2f}\nVocê está com sobrepeso.".format(calculo))
elif calculo < 40:
    print("O valor do seu IMC foi de {:.2f}\nVocê está com obesidade.".format(calculo))
elif calculo > 40:
    print("O valor do seu IMC foi de {:.2f}\nVocê está com obesidade mórbida.".format(calculo))
else:
    print("Comando Desconhecido.")
