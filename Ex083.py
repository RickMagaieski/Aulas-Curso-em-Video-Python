conto = 0
contc = 0

quest = str(input("Type an expression: "))

for run in quest:
    if run == '(':
        conto += 1
    elif run == ')':
        contc += 1

if conto == contc:
    print("Congrats! Your expression is valid :)")
else:
    print("Sorry... Your expression is invalid :(")
