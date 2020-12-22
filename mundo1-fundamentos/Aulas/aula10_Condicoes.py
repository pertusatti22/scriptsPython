# Condições simples e compostas
# Panda para extração de dados
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro Velho')
print('--FIM--')

'''tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <=3 else 'carro velho')
print('--FIM--')'''

#PRATICA
nome = str(input('Qual é seu nome?' ))
if nome == 'Jackson':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m>= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Estude mais!')