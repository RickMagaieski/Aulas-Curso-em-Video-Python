from random import randint

void = ''
numeros = []

for ran in range(0, 5):
    numeros.append(randint(0, 10))
print("\033[1mOs números sorteados foram:\033[m", end=' ')
for t in tuple(numeros):
    print(t, end=' ')
print(void)
print(f"\n\033[1mO maior valor sorteado foi: \033[m{max(tuple(numeros))}")
print(f"\033[1mO menor valor sorteado foi: \033[m{min(tuple(numeros))}")
