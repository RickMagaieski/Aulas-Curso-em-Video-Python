from time import sleep

casa = int(input("Valor da Casa: "))
sal = int(input("Salario do Comprador: "))
fina = int(input("Anos de Financiamento: "))

val = casa / (fina * 12)

print()

print(f"Para financiar um casa no valor de ${casa} em {fina} a prestacao sera de ${val:.2f}")

print()

if val > 30 * sal / 100:
    print("FINANCIAMENTO NEGADO")
    sleep(1)
    print("Infelizmente o seu perfil nao condiz com esta operacao...")
else:
    print("FINANCIAMENTO APROVADO!")
    sleep(1)
    print("O seu perfil condiz com esta operacao!")
