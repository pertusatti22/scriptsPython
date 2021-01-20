'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
print('-='*20)
print('10 Termos de uma PA - WHILE')
print('-='*20)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 9
while c != 0:
    primeiroTermo = primeiroTermo + razao
    print('{}'.format(primeiroTermo), end = ' => ')
    c -= 1
print('ACABOU')
print('-='*20)
print('Fim do Programa')
print('-='*20)