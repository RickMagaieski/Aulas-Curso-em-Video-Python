count = 0
listy = []
void = ''

while True:
    listy.append(int(input("Type a value: ")))
    count += 1
    ques2 = str(input("Do you want to continue? [Y/N] ")).upper()
    if ques2 == 'N':
        break
    if ques2 != 'Y' and 'N':
        print("Invalid Command!")
        break

listy.sort(reverse=True)

print(void)
print(f"You've typed {count} values.")
print(f"The values in descending order are: {listy}")
if 5 in listy:
    print("The value 5 is part of the list!")
else:
    print("The value 5 isn't part of this list...")
