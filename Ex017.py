from math import hypot
import emoji
n1 = float(input("Digite o valor do primeiro cateto: "))
n2 = float(input("Digite o valor do segundo cateto: "))
hi = hypot(n1,n2)
print(emoji.emojize("O valor da hipotenusa será {:.2f} :beaming_face_with_smiling_eyes:!").format(hi))
