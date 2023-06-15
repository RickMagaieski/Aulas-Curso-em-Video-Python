import math
di = float(input("Digite o valor do angulo que tu quer: "))
sen = math.sin(math.radians(di))
cos = math.cos(math.radians(di))
tan = math.tan(math.radians(di))
print("O ângulo inserido corresponde:\nPara o seno: {:.2f}\nPara o cosseno: {:.2f}\nPara a tangente: {:.2f}"
      .format(sen, cos, tan))
