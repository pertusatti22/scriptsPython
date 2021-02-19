'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele
marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.'''
#Funções
def ficha(jog = '<desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
nomeDoJogador = str(input('Nome do Jogador: '))
numeroDeGols = str(input('Número de gols: '))
if numeroDeGols.isnumeric():
    numeroDeGols = int(numeroDeGols)
else:
    numeroDeGols = 0
if nomeDoJogador.strip() == '':
    ficha(gol = numeroDeGols)
else:
    ficha(nomeDoJogador, numeroDeGols)