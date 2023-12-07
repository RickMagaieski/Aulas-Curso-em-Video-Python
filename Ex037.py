print()

num = int(input("Digite um numero inteiro: "))

print()

print("[ 1 ] converter para BINARIO\n"
      "[ 2 ] converter para OCTAL\n"
      "[ 3 ] converter para HEXADECIMAL")

print()

esc = int(input("Sua escolha: "))

print()

if esc == 1:
    print(f"O numero {num} digitado em BINARIO e igual a: {bin(num)}")
if esc == 2:
    print(f"O numero {num} digitado em OCTAL e igual a: {oct(num)}")
if esc == 3:
    print(f"O numero {num} digitado em HEXADECIMAL e igual a {hex(num)}")
