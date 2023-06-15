print("Seja muito bem vindo ao conversor de medidas!")
m1 = float(input("Dgite uma distância em metros: "))
mm = m1*1000
cm = m1*100
dm = m1*10
dma = m1/10
hm = m1/100
km = m1/1000
print("Os valores para a outras medidas serão essas respectivamente:"
      "\n{}km\n{}hm\n{}dma\n{}dm\n{}cm\n{}mm".format(km, hm, dma, dm, cm, mm))
