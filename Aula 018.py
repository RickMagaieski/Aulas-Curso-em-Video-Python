#Teoria:
"""
dados = ['Pedro', 25, 'Maria', 19, 'João', 35]
#dados.append('Pedro')
#dados.append(25)


lista = []
lista.append(dados[:])
print(lista[0][0]) #Pega dentro da estrutura 0 e procura o item 0, que no caso seria Pedro.
print(lista[0][1]) #Mesma coisa aqui, porém agora ele o item 1 dentro desse mesma estrutura, que no caso seria 25.

print(lista[1]) #Aqui ele pega toda a estrutura 1, sem separar o nome da idade ou vice e versa.


#Prática:

teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()

galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])

print(galera)

#O grande X da questão é o [:], sem isso você vai criar uma ligação entre as duas listas e vai duplicar as coisas.

#Existe essa forma de fazer também (que eu prefiro):
pessoal = [['João', 20], ['Ana', 12], ['Maria', 19], ['Paulo', 32]]

for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos')


galera = list()
void = ''
dados = list()
totalmen = totalmai = 0

for c in range(0, 3):
    dados.append(str(input("Digite seu nome: ")))
    dados.append(int(input("Digite sua idade: ")))
    print(void)
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} maior de idade.")
        totalmai += 1
    else:
        print(f"{p[0]} menor de idade")
        totalmen += 1
print(void)
print(f"Temos {totalmai} maior(es) de idade e {totalmen} menor(es) de idade")"""
