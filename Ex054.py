from datetime import date
data = date.today().year
contv = 0
contn = 0
for i in range(1, 8):
    pergunta = int(input(f"\033[1mEm que ano a {i}ª pessoa nasceu? \033[m"))
    conta = data - pergunta
    print(F"\033[1m\033[4;36mIdade atual\033[m\033[m: \033[1;36m{conta}\033[m")
    if conta >= 18:
        contv += 1
    else:
        contn += 1
print(f"\033[1mAo todo foram \033[m\033[1m\033[1;36m{contv}\033[m \033[1mpessoas com mais de\033[m \033[1;36m18"
      f"\033[m \033[1manos.\033[m ")
print(f"\033[1mE \033[m\033[1;36m{contn}\033[m\033[1m pessoas com menos de \033[m\033[1;36m18\033[m\033[1m anos.\033[m")
