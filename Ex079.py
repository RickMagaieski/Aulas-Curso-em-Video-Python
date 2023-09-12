listy = []
ques2 = ''
void = ''

while True:
    ques = int(input("Type a number: "))
    if ques not in listy:
        listy.append(ques)
    else:
        print("Value already typed! Type another one.")
    ques2 = str(input("You want continue? [Y/N] ")).upper()
    if ques2 == 'N':
        break
    if ques2 != 'Y':
        print("Invalid Command")
        break
print(void)
if ques2 == 'N':
    print(f"You've added these values: {sorted(listy)}")
if ques2 != 'N' or 'Y':
    print("Program Finished")
