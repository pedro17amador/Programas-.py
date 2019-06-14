from math import hypot
oposto = int(input('Digite um cateto oposto: '))
adjacente = int(input('Digite um cateto adjacente: '))
print('O cateto oposto é {} e o cateto adjacente é {} então sua hipotenusa será {:.0f}'.format(oposto, adjacente ,hypot(oposto, adjacente)))