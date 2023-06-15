#pergunta = float(input("Quantos Km seu carro já andou? "))
#
#if pergunta > 20.000:
    #print(f"Seu carro já rodou mais de {km}Km, por isso ele não se enquadra como semi-novo.")
#else:
    #print(f"Seu carro pode ser considerado como semi-novo pois ele não ultrapassou os {km}Km")
#print("---Fim---")
import emoji
n1 = float(input("Digite a primeira nota final do semestre: "))
n2 = float(input("Digite a segundo nota final do semestre: "))
media = (n1 + n2)/2
print("Sua nota foi de {:.1f}".format(media))
if media >= 6:
    print("Parabéns, você passou de ano, continue assim 🤩!")
else:
    print("Infelizmente você reprovou, tente melhorar no próximo ano 😢!")
print("A todos um maravilhoso fim de ano!")
