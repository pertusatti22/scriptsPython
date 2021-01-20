'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('-='*20)
print('Jogo do Par ou impar')
print('-='*20)
contador = 0
while True:
    jogador = -1
    while jogador not in range(0,10):
        jogador = int(input('Digite um valor de 0 a 10: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar?[P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {contador} vezes!')
print('-='*20)
print('Fim do Programa')
print('-='*20)