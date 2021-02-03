'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
print('-'*30, '\n{:^30}\n'.format('JOGA NA MEGA SENA'), '-'*30)
from random import randint
from time import sleep
lista = list()
jogos = list()
palpites = int(input('Quantos jogos você quer que eu sorteie? '))
t = 1
while t <= palpites:
    contador = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador +=1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    t += 1
print('-='*3, f' SORTEANDO {palpites} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*6, f'   <  BOA SORTE!  >   ', '-='*6)