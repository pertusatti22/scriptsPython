from random import randint
computador = randint(0, 5)
print ('\033[1;31;40m-=-\033[m' * 20)
print('\033[0;35;41mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print ('-=-' * 20)
jogador = int(input('Em que número pensei? '))
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
#depois refatorar adicionando cores no terminal.