print("="*19)
print("Seja bem vindo!")
print("="*19)
v1 = float(input("Digite o valor do primeiro segmento: "))
v2 = float(input("Digite o valor do segundo segmento: "))
v3 = float(input("Digite o valor do terceiro segmento: "))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print("Esses valor conseguem criar um triângulo!")
else:
     print("Infelizmente esses valores não conseguem criar um triângulo...")
