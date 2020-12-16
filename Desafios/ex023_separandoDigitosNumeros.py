numero = int(input('Digite um número: '))
print('Analisando o número {}'.format(numero))
analise = numero // 1 % 10
print('Unidade: {}'.format(analise))
analise = numero // 10 % 10
print('Dezena: {}'.format(analise))
analise = numero // 100 % 10
print('Centena: {}'.format(analise))
analise = numero // 1000 % 10
print('Milhar: {}'.format(analise))