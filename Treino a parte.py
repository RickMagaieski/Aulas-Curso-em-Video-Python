from datetime import datetime
from time import sleep


def oi():
    for oil in range(0, 11, 2):
        sleep(0.5)
        print(oil)


oi()
print("FIM")
sleep(1)
print("Gostaria de resetar a contagem?\nSim\nNão ")
perg = input("Sua resposta: ")
dia = datetime.now().hour
if perg == "sim":
    oi()
elif perg == "não" and dia < 18:
    print("Certo! Tenha um bom dia.")
else:
    print("Certo! Tenha uma ótima noite.")
