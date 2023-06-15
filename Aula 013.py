from time import sleep
"""print("T-")
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print("Lançar!!!!")"""
s = 0
for c in range(0, 4):
    valor = int(input("Digite um valor: "))
    s += valor
print("End")
print(f"O valor final foi {s}")
