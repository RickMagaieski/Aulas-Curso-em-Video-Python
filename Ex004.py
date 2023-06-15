n = input("\033[1mOlá! Qual é o seu nome? ")
if n == 'Henrique' or n == 'henrique':
    print("Seja muito bem vindo {}!".format(n))
    d = input("Digite algo: ")
    print("\033[1m\033[4;36mO tipo primitivo desse valor é:\033[m",  type(d))
    print("\033[1;34m\033[4mÉ composto somente por espaços?\033[m", d.isspace())
    print("\033[1;34m\033[4mÉ um número?\033[m", d.isnumeric())
    print("\033[1;34m\033[4mÉ alfabétco?\033[m", d.isalpha())
    print("\033[1;34m\033[4mÉ alfanúmerico?\033[m", d.isalnum())
    print("\033[1;34m\033[4mEsta em letras maiúsculas?\033[m", d.isupper())
    print("\033[1;34m\033[4mEstá em letras minúsculas?\033[m", d.islower())
else:
    print("\033[1;31mPerdão, não podemos continuar.\033[1;31m")
