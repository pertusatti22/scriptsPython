'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. '''
print('-'*20)
print('Lista de Compra')
print('-'*20)
produto = final = barato = ' '
preço = total = produtoMil = preçoBarato = cont = 0
while True:
    produto = str(input('Insira o nome do Produto: '))
    preço = float(input('Insira o valor do preço do Produto: R$ '))
    cont += 1
    total += preço
    if cont == 1 or preço < preçoBarato:
        barato = produto
        preçoBarato = preço
    if preço > 1000:
        produtoMil += 1
    while final not in 'SN':
        final = str(input('Deseja inserir mais produtos? [S/N] ')).upper().strip()[0]
    if final == 'N':
        print(f'O gasto total de sua compra foi de R$ {total:.2f}.')
        print(f'Você comprou {produtoMil} com preço acima de R$ 1.000,00.')
        print(f'O produto mais barato da lista é {barato} e custou {preçoBarato:.2f}.')
        break
    else:
        final = produto = ' '
        preço = 0
print('-'*20)
print('Fim do Programa')
print('-'*20)