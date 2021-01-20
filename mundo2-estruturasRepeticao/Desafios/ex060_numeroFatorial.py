#from math import factorial 'f = factorial (n)'
'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
print('-='*20)
print('Fatorial')
print('-='*20)
numero = int(input('Digite um número para\ncalcular seu Fatorial: \n'))
c = numero
f = 1
print('Calculando {}! = '.format(numero), end='')
while c > 0:
    print ('{}'.format(c), end='')
    print (' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
for c in range (f, numero):
    print ('{}'.format(c), end='')
    print (' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print ('{}'.format(f))
print('-='*20)
print('Fim do Programa')
print('-='*20)