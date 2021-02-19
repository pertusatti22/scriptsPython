'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior.'''
def maior(* valores):
    c = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in valores:
        print(f'{valor} ', end='')
        if c == 0:
            maior = valor
        else:
            if valor>maior:
                maior = valor
        c+=1
    print(f'\nForam informandos{c} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()