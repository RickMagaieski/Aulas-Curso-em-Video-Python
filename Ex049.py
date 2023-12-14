print("=" * 25)
print(f"{'SUA TABUADA':>17}")
print("=" * 25)

print()

n = int(input("Que tabuada vc quer ver? "))

print()

for t in range(1, 11):
    print(f"{n} X {t} = {n * t}")
