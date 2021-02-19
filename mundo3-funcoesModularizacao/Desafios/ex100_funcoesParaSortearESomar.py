'''Exercício Python 100: Faça um programa que tenha uma lista 
chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro
da lista e a segunda função vai mostrar a soma entre todos os 
valores pares sorteados pela função anterior.'''
from random import randint

def sorteia(dezenas):
    for i in range(0, 5):
        dezenas.append(randint(1, 9))
        i += 1
    print(f'Sorteando 5 valores da lista: {dezenas} PRONTO!')

def somaPar(dezenas):
    soma = 0
    for c in dezenas:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {dezenas}, temos {soma}')


números = list()
sorteia(números)

somaPar(números)