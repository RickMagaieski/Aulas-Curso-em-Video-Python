print("Comparador de Números")
num1 = int(input("Digite um primeiro número: "))
num2 = int(input("Digite um segundo número: "))
if num1 > num2:
    print(f"O número maior entre esses dois é o número {num1}!")
elif num2 > num1:
    print(f"O número maior entre esses dois é o número {num2}!")
else:
    print("Ambos os números são iguais!")
