no = input("Olá, digite antes de tudo o seu nome: ")
print("Seja muito bem vindo {} ao sistema de notas!".format(no))
cod = input("Antes de você lançar as notas preciso saber se você é um professor cadastrado."
            "\nDigite seu código de confirmação: ")
print("Maravilha, o código {} foi confirmado!".format(cod))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
print("A média dos número {:.1f} e {:.1f} deste aluno foi de {:.1f}".format(n1, n2, m))
