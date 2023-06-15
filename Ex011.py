l = float(input("Qual é a largura da parede? "))
a = float(input("Qual é a altura da parede? "))
ar = l*a
dis = ar/2
print("Sua parede tem a dimensão de {} X {} e sua área é de {}m².\nPara pintar essa parede, "
      "você preicsará de {}L de tinta.".format(l, a, ar, dis))
