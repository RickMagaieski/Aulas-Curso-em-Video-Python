"""import math
num = float(input("Digite um número quebrado: "))
print("O valor definido foi {} e sua porção inteira é {}".format(num, math.floor(num)))"""
from math import trunc
p = float(input("Digite um número quebrado: "))
print("O número digitado foi {} e seu valor inteiro é {}.".format(p, trunc(p)))
