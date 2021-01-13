'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela.
Seu programa deverá realizar a operação solicitada em cada caso. '''
print('-='*20)
print('Menu de Opções')
print('-='*20)
opcao = 0
while opcao != 5:
    primeiroValor = int(input('Primeiro valor: '))
    segundoValor = int(input('Segundo valor: '))
    opcao = int(input('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    >>>>> Qual é a sua opção: '''))
    if opcao == 1:
        print('A soma entre {} + {} é  {}'.format(primeiroValor, segundoValor, primeiroValor+segundoValor))
    elif opcao == 2:
        print('A multiplicação entre {} * {} é  {}'.format(primeiroValor, segundoValor, primeiroValor*segundoValor))
    elif opcao == 3:
        print('O maior número entre {} e {} é  {}'.format(primeiroValor, segundoValor, max(primeiroValor,segundoValor)))
    elif opcao == 4:
        print('Selecione novos números!')
    elif opcao == 5:
        print('Saindo do Programa!')
    else:
        print('Opção Inválida! tente novamente.')
print('-='*20)
print('Fim do Programa')
print('-='*20)