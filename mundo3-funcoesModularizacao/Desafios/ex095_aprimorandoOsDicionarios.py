'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
baseDeJogadores = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    total = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, total):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    baseDeJogadores.append(jogador.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper()[0]
        if resposta not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
        else:
            break
    if resposta == 'N':
        break
#resultados
print('-='*40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(baseDeJogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(baseDeJogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {baseDeJogadores[busca]["nome"]}:')
        for i, g in enumerate(baseDeJogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-'*40)
print(' << VOLTE SEMPRE >> ')