print("CCONVERSOR DE MEDIDAS COMPUTACIONAIS")
num = int(input("Digite um número decimal qualquer: "))
print("Para qual sistema você gostaria de converter seu número?")
print("[1] Binário.\n[2] Octal.\n[3] Hexadecimal.")
escolha = int(input("Faça sua escolha: "))
if escolha == 1:
    conversao = bin(num)[2:]
    print(f"O número {num} escrito em Binário fica da seguinte forma: {conversao}")
elif escolha == 2:
    conversao = oct(num)[2:]
    print(f"O número {num} escrito em Octal fica da seguinte forma: {conversao}")
elif escolha == 3:
    conversao = oct(num)[2:]
    print(f"O número {num} escrito em Hexadecimal fica da seguinte forma: {conversao}")
else:
    print("Comando Desconhecido.")
