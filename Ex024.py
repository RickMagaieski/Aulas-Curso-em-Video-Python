print("Esse programa funcionará apenas se você residir em alguma cidade contendo no nome a palavra Santo(s)")
per = str(input("Em que cidade você mora? ")).strip().upper().lower()
#print('santo' in per)
if per == 'Santos' or per == 'santo' or per == 'Santo' or per == 'santos':
    print("Seja bem vindo!")
else:
    print("Acesso negado.")
