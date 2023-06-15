nome = str(input("Digite o seu nome completo meu fio: ")).strip()
n = nome.split()
print(f"O seu primeiro nome é: {n[0]}\nE o seu último nome é: {n[len(n)-1]}")
