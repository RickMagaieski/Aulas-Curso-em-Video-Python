listy = []

for values in range(0, 5):
    num = int(input("Type an value: "))
    if values == 0 or num > listy[-1]:
        listy.append(num)
    else:
        pos = 0
        while pos < len(listy):
            if num <= listy[pos]:
                listy.insert(pos, num)
                break
            pos += 1
print(f"The ordened numbers are: {listy}")
