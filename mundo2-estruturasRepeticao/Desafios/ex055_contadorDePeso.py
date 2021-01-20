'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''
print('-='*20)
print('Balança')
print('-='*20)
base = []
for c in range(1,6):
    peso = float(input('Quantos kilos a {}º pessoa pesa? '.format(c)))
    base.append(peso)
print('O maior peso lido foi de {:.1f}Kg\nO menor peso lido foi de {:.1f}Kg'.format(max(base),min(base)))
print('-='*20)
print('Fim do Programa')