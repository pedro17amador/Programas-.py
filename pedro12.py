altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
m = altura*largura
d = m/2
print('Sua parede tem área de {} metros quadrados e para pintar a parede você vai precissar de {:.3}L de tinta.'.format(m, d))

