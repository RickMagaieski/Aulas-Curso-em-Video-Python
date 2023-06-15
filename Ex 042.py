v1 = float(input("Digite o valor do primeiro segmento: "))
v2 = float(input("Digite o valor do segundo segmento: "))
v3 = float(input("Digite o valor do terceiro segmento: "))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print("Esses valores conseguem criar um triângulo", end='')
    if v1 == v2 == v3:
        print(" EQUILÁTERO.")
    elif v1 != v2 != v3 and v1 != v3:
        print(" ESCALENO.")
    else:
        print(" ISÓSCELES.")
else:
     print("Infelizmente esses valores não conseguem criar um triângulo...")
