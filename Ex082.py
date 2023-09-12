listy = []
even = []
odd = []
void = ''

while True:
    ques = int(input("Type a value: "))
    ques2 = str(input("Do you want to continue? [Y/N] ")).upper()
    listy.append(ques)
    if ques % 2 == 0:
        even.append(ques)
    if ques % 2 == 1:
        odd.append(ques)
    if ques2 == 'N':
        break
    if ques2 != 'Y' and 'N':
        print("Invalid Command!")
        break

print(void)
print(f"The orginal list is this: {listy}")
print(void)
print(f"The even list is this: {even}")
print(f"And the odd list is this: {odd}")
