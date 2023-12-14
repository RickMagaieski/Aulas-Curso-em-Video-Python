from time import sleep

print()
cont = 0

for p in range(0, 52, 2):
    cont += 1
    if cont % 2 == 0:
        print(f"\033[1m{p}\033[m", end='  ')
    if cont % 2 != 0:
        print(f"\033[1;31m{p}\033[m", end='  ')

print("\033[1;31mAcabou\033[m")
