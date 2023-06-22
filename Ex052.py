perg = int(input("Digite um número: "))
count = 0
for c in range(1, perg + 1):
    if perg % c == 0:
        print("\033[31m", end=' ')
        count += 1
    else:
        print("\033[32m", end=' ')
    print(c, end='')
print(f"\n\033[mO número \033[31m{perg}\033[m foi divisivel \033[31m{count}\033[m vezes.")
if count == 2:
    print("Por isso ele É primo!")
else:
    print("Por isso ele NÃO É primo.")
