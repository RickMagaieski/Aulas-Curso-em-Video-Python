from time import sleep
from datetime import datetime
print("\033[1m!! 🎆 CONTAGEM REGRESSIVA PARA 2024 🎆 !!\033[m")
tempo1 = datetime.now().hour
tempo2 = datetime.now().minute
tempo = f"{tempo1:02d}:{tempo2:02d}"
if tempo1 == 16 and tempo2 == 20:
    print("\033[1mContagem iniciada")
    sleep(0.5)
    for c in range(10, -1, -1):
        sleep(1)
        print("\033[1m",c ,"\033[m")
    sleep(0.5)
    print("\033[1;34m!!! 🎆🎆🎆 Feliz Ano Novo 🎆🎆🎆 !!!\033[1;34m")
else:
    print("\033[1;31mO tempo está incorreto.\033[m")
    sleep(1)
    print(f"\033[1mHorário atual: {tempo}\033[m")
