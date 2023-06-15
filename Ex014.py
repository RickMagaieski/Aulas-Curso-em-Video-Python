t = float(input("Digite a temperatura desejada em °C: "))
f = (t*9/5) + 32
k = t+273.15
print("A temperatura de {} em °C é equivalente a {:.2f}°F e a {:.2f}°K, respectivamente.".format(t, f, k))
