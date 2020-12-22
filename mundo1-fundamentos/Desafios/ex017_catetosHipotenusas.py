from math import hypot
catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {}'.format(hypot(catetoAdjacente, catetoOposto)))
