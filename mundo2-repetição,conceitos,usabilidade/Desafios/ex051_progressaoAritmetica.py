'''Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a 
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''
print('-='*20)
print('10 Termos de uma PA')
print('-='*20)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiroTermo + 10 * razao
for c in range (primeiroTermo, decimoTermo, razao):
    print('{}'.format(c), end = ' -> ')
print('ACABOU')
print('-='*20)
print('Fim do Programa')
print('-='*20)