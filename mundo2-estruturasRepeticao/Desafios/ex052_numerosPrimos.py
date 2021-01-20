'''Exercício Python 52: Faça um programa que leia um número 
inteiro e diga se ele é ou não um número primo. '''
print('-='*20)
print('Número Primos')
print('-='*20)
contador = 0
numero = int(input('Insira um número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end=' ')
        contador += 1
    else:
        print('\033[m', end=' ')
    print('{} '.format(c), end=' ')
print('\nO número {} foi divisível {} vezes!\n'.format(numero, contador), end=' ')
if contador == 2:
    print('E por isso ele é PRIMO!')
else:
    print('Sendo assim, ele NÃO é primo!')
print('-='*20)
print('Fim do Programa')
print('-='*20)