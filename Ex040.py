print("""[ 1 ] Matemática 
[ 2 ] Português
[ 3 ] História""")
mater = int(input("Qual materia você gostaria de selecionar ? "))
if mater == 1:
    print("Você selecionou Matematica.")
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7.0:
        print("Parabéns, a sua média foi de {:.1f} ! Você foi APROVADO.".format(media))
    elif 5.0 <= media < 6.9:
        print("A sua média foi de {:.1f}, terá que ficar de recuperação... estude mais da próxima.".format(media))
    else:
        print("A sua média foi de {:.1f}, portanto você reprovou. Estude mais!".format(media))
elif mater == 2:
    print("Você selecinou Português.")
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceria nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7.0:
        print("Parabéns, a sua média foi de {:.1f} ! Você foi APROVADO.".format(media))
    elif 5.0 <= media < 6.9:
        print("A sua média foi de {:.1f}, terá que ficar de recuperação... estude mais da próxima.".format(media))
    else:
        print("A sua média foi de {:.1f}, portanto você reprovou. Estude mais!".format(media))
elif mater == 3:
    print("Você selecionou História.")
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota3 = float(input("Digite a sua terceria nota: "))
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7.0:
        print("Parabéns, a sua média foi de {:.1f} ! Você foi APROVADO.".format(media))
    elif 5.0 <= media < 6.9:
        print("A sua média foi de {:.1f}, terá que ficar de recuperação... estude mais da próxima.".format(media))
    else:
        print("A sua média foi de {:.1f}, portanto você reprovou. Estude mais!".format(media))
else:
    print("Comando Desconhecido.")
