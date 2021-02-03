'''Exercício Python 076: Crie um programa que tenha uma tupla única 
com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in listagem:
    if type(item) is str:
        print(f'{item:.<32}',end ='')
    else:
        print(f'R${item:>7.2f}')
print('-'*40)
