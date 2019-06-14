preço = float(input('Preço do produto: '))
desconto = preço-(preço*10/100)
aumento = preço+(preço*8/100)
print('O preço do produto a vista com 10% de desconto sai por R${:.2f}\nO preço do produto parcelado com 8% de aumento sai por R${:.2f}'.format(desconto, aumento))



