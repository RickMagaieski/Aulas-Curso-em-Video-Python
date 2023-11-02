l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

print()

if l2 + l3 > l1 and l1 + l3 > l2 and l2 + l1 > l3:
    print("Os segmentos acima podem formar um triângulo.")
else:
    print("Os segmentos acima não podem formar um triângulo.")