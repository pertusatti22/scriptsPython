#litro de tinta = 2m²
largura = int(input('Qual é a largura da parede em metros? '))
altura = int(input('Qual é a altura da parede em metros? '))
areaTotal = largura * altura
tinta = areaTotal/2

print('A área total da parede é {} metros, e a quantidade de tinta para pintá-la é de {} litros'.format(areaTotal,tinta))