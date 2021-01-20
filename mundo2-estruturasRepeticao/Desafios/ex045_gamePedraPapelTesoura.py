from random import randint
print('-='*20)
print('SUPER JOGUINHO DE JOKEMPÔ')
print('-='*20)
jogador = str(input('\nInsira seu nome: '))
jokempo = ['pedra','papel','tesoura']
print('\n N | Jokempô\n 1 | {}\n 2 | {}\n 3 | {} \n'.format(jokempo[0],jokempo[1],jokempo[2]))
placar = False
placarJogador = 0
placarAdversario = 0
while not placar:
    if (placarAdversario >=100) or (placarJogador >= 100):
        break
    else:
        placar = False
    pontos = randint(10,25)
    print('Esta jogada vale {} pontos, {}!'.format(pontos, jogador))
    valida = False
    while not valida:
        jogada = int(input('Insira a sua jogada, utilizando um dos Números: '))
        if jogada > 0 and jogada <= 3:
            jogada = jogada - 1
            break
        else:
            print('Opção inválida!')
            valida = False
    print('-='*20)
    print('\nJO-KEM-PÔ!!!\n')
    print('-='*20)
    adversario = randint(0,2)
    print('O adversário jogou: {}'.format(jokempo[adversario]))
    print('O {} jogou: {}'.format(jogador,(jokempo[jogada])))
    if adversario == jogada:
        print('EMPATE!!! ninguém obteve pontuação')
        print('O placar atual é:\n{} - {} Pontos | Adversário - {} Pontos'.format(jogador, placarJogador, placarAdversario))
    elif adversario == 0 and jogada == 2 or adversario == 1 and jogada == 0 or adversario == 2 and jogada == 1:
        print('PERDEU!!! adversário marcou {} pontos!'.format(pontos))
        placarAdversario = placarAdversario + pontos
        print('O placar atual é:\n{} - {} Pontos | Adversário - {} Pontos'.format(jogador, placarJogador, placarAdversario))
    else:
        print('GANHOU!!! você marcou {} pontos!'.format(pontos))
        placarJogador = placarJogador + pontos
        print('O placar atual é:\n{} - {} Pontos | Adversário - {} Pontos'.format(jogador, placarJogador, placarAdversario))
print('FIM DE JOGO!!!')
print('O placar FINAL é:\n{} - {} Pontos | Adversário - {} Pontos'.format(jogador, placarJogador, placarAdversario))
if placarAdversario > placarJogador:
    print('Você perdeu! TENTE NOVAMENTE!!!')
elif placarAdversario < placarJogador:
    print('Você ganhou! PARABÉNS! VOCÊ É GENIAL!!!')
else:
    print('Essa não! jogo empatado, TENTE NOVAMENTE!!!')

print('-='*20)
print('Fim do Programa')
print('-='*20)