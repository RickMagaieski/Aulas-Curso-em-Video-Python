from time import sleep

print("{:^40}".format("=" * 30))
print("{:^40}".format("Banco Magaieski's"))
print("{:^40}".format("=" * 30))
void = ''

print(void)
conta = int(input("Quanto saldo você tem? R$"))
print(void)
print("=" * 39)
while True:
    di = int(input('Digite quanto você deseja sacar: R$'))
    n50 = n20 = n10 = n1 = 0
    saldo = conta - di
    while True:
        if di >= 50:
            di -= 50
            n50 += 1
        elif di >= 20:
            di -= 20
            n20 += 1
        elif di >= 10:
            di -= 10
            n20 += 1
        elif di >= 1:
            di -= 1
            n10 += 1
        else:
            break
    print("Você sacou:")
    print(f"{n50} notas de R$50\n{n20} notas de R$20\n{n10} notas de R$10\n{n1} notas de R$1")
    print(f"Seu saldo agora é de {saldo}")
    conta = saldo
    sleep(1)
    perg = str(input("Deseja continuar? [S/N] ")).upper()
    if perg == 'N':
        print("=" * 30)
        print("{:^30}".format("Volte sempre!"))
        break
