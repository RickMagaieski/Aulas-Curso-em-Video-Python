#Treino sobre cores no terminal:

from random import choice
from time import sleep
print("\033[1mSeja bem vindo!")
ques = input(str("Vamos jogar um jogo? \033[m"))
if ques == "Sim" or ques == "sim" or ques == "SIM":
    print("\033[1;31mMaravilha!!\033[m")
    game = input(str("\033[1mEntão, eu irei precisar que vc digite algo... algo curto: "))
    print("Ótimo, agora eu vou escolher uma letra da sua palavra\nE vc vai precisar advinhar qual é! ")
    guess = input(str("Advinhe... se conseguir: "))
    ch = choice(game)
    if guess == ch:
        print("\033[1;32mParabéns! Você adivinhou!!\033[1m")
    else:
        print("\033[1;31mQue pena... você não advinhou...\nTente de novo, talvez agora você consiga!\033[m")
else:
    print("\033[1;37mOk, sem problema, te vejo outra hora!\033[m")
