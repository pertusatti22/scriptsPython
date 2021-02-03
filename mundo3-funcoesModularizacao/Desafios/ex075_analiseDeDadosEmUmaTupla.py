'''Exercício Python 075: Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

valores = (int(input('Digite o 1º valor: ')),int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('\nNão foram digitados números pares')
        break