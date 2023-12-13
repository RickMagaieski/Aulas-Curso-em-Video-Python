print()

l1 = float(input("Primeiro Segmento: "))
l2 = float(input("Segundo Segmento: "))
l3 = float(input("Tercerio Segmento: "))

print()

if l2 + l3 > l1 and l1 + l3 > l2 and l1 + l2 > l3:
    print("Eles podem formar um triangulo!")
else:
    print("Eles nao podem formar um triangulo...")

if l1 == l2 == l3:
    print("E esse triangulo sera um triangulo EQUILATERO!")
elif l1 != l2 != l3 != l1:
    print("E esse triangulo sera um triangulo ESCALENO!")
elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
    print("E esse triangulo sera um triangulo ISOSCELES")
