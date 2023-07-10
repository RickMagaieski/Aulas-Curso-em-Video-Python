usuario = input("Digite algo: ").strip().upper()
palavra = usuario.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print(f"O inverso da palvra digitada é {inverso}")
if junto == inverso:
    print("São a mesma coisa, por isso é um palíndromo!")
else:
    print("São diferentes, por isso não é um palíndromo...")
