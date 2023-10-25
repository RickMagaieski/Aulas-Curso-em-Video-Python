lista = []

ex = str(input("Digite sua expressão: "))

for v in ex:
    if v == '(':
        lista.append(v)
    elif v == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break


if len(lista) == 0:
    print("Sua expressão está correta!")
else:
    print("Sua expressão está incorreta...")
