while True:
    n = int(input("Voce deseja ver qual tabuada? "))

    print("=" * 30)

    print()

    if n <= 0:
        break

    for tab in range(1, 11):
        print(f"{n} X {tab} = {n * tab}")

    print()

    print("=" * 30)

print("O programa TABUADA foi encerrado com sucesso!")
