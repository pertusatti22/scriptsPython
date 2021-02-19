'''Exercício Python 097: Faça um programa que tenha uma função chamada 
escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.                                  
Ex:
escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~'''
def escreva(mensagem):
    a = len(mensagem) + 6
    print('~' * a)
    print(f' > {mensagem} <')
    print('~' * a)


escreva('Jackson Pertusatti')
escreva('Curso de Python no Youtube')
escreva('CeV')