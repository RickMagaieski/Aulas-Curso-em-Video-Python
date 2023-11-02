void = ''

print(void)

vel = int(input("\033[1mDigite a velocidade atual do carro:\033[m "))

multa = (vel - 80) * 7.00

print(void)

if vel > 80:
    print(f"\033[31mMULTADO! Você ultrapassou o limite de velocidade que é de 80Km/h."
          f"\nVocê deve pagar uma multa de\033[m \033[33m${multa:.2f}!\033[m")
else:
    print("\033[32mVelocidade dentro do limite. Tenha um ótimo dia!\033[m")
