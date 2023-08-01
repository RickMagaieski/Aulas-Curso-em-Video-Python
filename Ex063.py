from time import sleep

print("=" * 22)
print("SEQUÊNCIA DE FIBONACCI")
print("=" * 22)
seq = int(input("Digite quantos termo da sequência você quer ver: "))
t1 = 0
t2 = 1
print(f"{t1} -> ", end='')
print(f"{t2}", end='')
cont = 3
void = ''
while cont <= seq:
    t3 = t1 + t2
    sleep(0.5)
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3
    cont += 1
print(" -> FIM")
