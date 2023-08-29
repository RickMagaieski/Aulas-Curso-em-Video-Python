numbers = []
void = ''
cont = 0
paircont = 0

for c in range(1, 5):
    quest = int(input("Type a number: "))
    numbers.append(quest)
    if quest == 9:
        cont += 1
    if quest % 2 == 0:
        paircont += 1
tupla = tuple(numbers)
print(f"You typed these numbers: {tupla}")
print(void)
print(f"The number 9 appeared {cont} time(s)")
if 3 in numbers:
    print(f"The first number 3 was typed in the {numbers.index(3) + 1} position")
else:
    print(f"There was no number 3")
print(f"The number of even numbers was {paircont}")
