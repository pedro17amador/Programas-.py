n1=float(input('Digite um número em metros: '))
km = n1*0.001
hm = n1*0.01
dam = n1*0.1
m = n1*1
dm = n1*10
cm = n1*100
mm = n1*1000
print('{:.0f} Metros tem \n{} Quilômetros \n{} Hectômetros \n{:.1f} Decâmetros \n{:.0f} Decímetros \n{:.0f} Centímetros e \n{:.0f} Milímetros'.format(n1, km, hm, dam, dm, cm, mm))