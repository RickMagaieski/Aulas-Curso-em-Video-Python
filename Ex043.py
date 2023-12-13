peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print()

print(f"O seu IMC foi de {imc:.2f}")

if imc <= 18.5:
    print("De acordo com o seu IMC, voce esta seco.")
elif imc <= 25:
    print("De acordo com o seu IMC, voce esta normal.")
elif imc <= 30:
    print("De acordo com o seu IMC, voce esta gordo.")
elif imc <= 40:
    print("De acordo com o seu IMC, voce esta obeso.")
elif imc > 40:
    print("De acordo com o seu IMC... novo planeta descoberto!!")
