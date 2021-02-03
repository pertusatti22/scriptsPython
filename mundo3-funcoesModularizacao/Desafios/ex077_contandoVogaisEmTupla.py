'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
palavras = ('abacate', 'goblin', 'senhor', 'duque', 'paladino')
for c in palavras:
    print(f'\n{c} tem as seguintes vogais: ', end='')
    for vogal in c:
        if vogal.lower() in 'aeiou':
            print(vogal, end='')