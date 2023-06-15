no = input("Seja bem vindo! Qual é o seu nome? ")
print(f"Prazer em te conhecer {no}")
print("Iremos fazer alguns calculos aleátorios, digite alguns números e veja o que sai :)")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
m = n1*n2
d = m/n1
s = d+n2
print("O resultado será: {}".format(s))

#Só rascunhos da aula

print("Olá seja bem vindo a calculadora de média!Por gentileza, digite a nota recebida"
      " em cada matéria a seguir para receber a média geral do semestre.")
m = int(input("Nota em Matemática: "))
p = int(input("Nota em Português: "))
h = int(input("Nota em História: "))
g = int(input("Nota em Geografia: "))
i = int(input("Nota em Inglês: "))
ed = int(input("Nota em Ed.Física: "))
a = int(input("Nota em Artes: "))
c = int(input("Nota em Ciências: "))
m = (m+p+h+g+i+ed+a+c)/8
print("Sua média semestral foi {:.2}".format(m))
