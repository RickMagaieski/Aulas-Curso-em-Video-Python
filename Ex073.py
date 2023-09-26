uni = ("Harvard", "MIT", "Stanford", "UC Berkeley", "Caltech", "Oxford", "Cambridge", "Chicago",
       "Imperial College London", "ETH Zurich", "UPenn", "Yale", "Princeton", "Cornell", "UCLA", "UC San Diego",
       "Columbia", "UW", "Edinburgh", "Tokyo")
void = ''

print(void)
print("\033[1m\033[4mLista das melhores universidade do mundo:\033[m\033[m")
print(void)

for u in uni:
    print('\033[1m*\033[m', u)

print(void)
print("\033[1m\033[4mAs 5 primeiras universidades são:\033[m\033[m")
print(void)

for pu in uni[0:5]:
    print('\033[1m*\033[m', pu)

print(void)
print("\033[1m\033[4mAs últimas 4 são:\033[m\033[m")
print(void)

for p in uni[-4:]:
    print('\033[1m*\033[m', p)

print(void)
print("\033[1m\033[4mUniversidades em ordem alfabética:\033[m\033[m")
print(void)

for univ in sorted(uni):
    print('\033[1m*\033[m', univ)
