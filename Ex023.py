n1 = int(input("Digite um número aí meu fio: "))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f"Analisando o número {n1} podemos ver o seguinte:")
print(f"Existe {u} unidade(s) neste número\nExiste {d} dezena(s) neste número\n"
      f"Existe {c} centena(s) neste número\nExiste {m} centena(s) neste número")
