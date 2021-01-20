'''Exercício Python 48: Faça um programa que calcule
a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''
from time import sleep
print('-='*20)
print('Multiplos de 3')
print('-='*20)
#Somatório
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('\nA soma de todos os {} valores solicitados é {}\n'.format(cont, soma))
print('-='*20)
print('Fim do Programa')
print('-='*20)