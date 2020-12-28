'''Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
print('-='*20)
print('Maioridade')
print('-='*20)
maior = 0
data = date.today().year
for c in range(1,8):
    nascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if data-nascimento >= 21:
        maior +=1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(maior, 7-maior))    
print('-='*20)
print('Fim do Programa')
print('-='*20)