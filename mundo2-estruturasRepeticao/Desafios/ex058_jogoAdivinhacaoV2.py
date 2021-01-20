'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print('-='*20)
print('Jogo de Adivinhação V 2.0')
print('-='*20)
computador = randint(0,10)
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
acerto = False
contador = 0
while not acerto:
    contador += 1
    jogador = int(input('Qual é seu palpite? '))
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    elif jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Acertou com {} tentativas. Parabéns!'.format(contador))
        break
print('-='*20)
print('Fim do Programa')
print('-='*20)