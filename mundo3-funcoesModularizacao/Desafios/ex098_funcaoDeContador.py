'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar 
três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        print('Você inseriu um passo inválido!')
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='', flush = False)
            sleep(0.2)
            c += passo
        print('FIM!')
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='', flush = False)
            sleep(0.2)
            c -= passo
        print('FIM!')

def escreva(mensagem):
    a = len(mensagem) + 6
    print('~' * a)
    print(f' > {mensagem} <')
    print('~' * a)


escreva('Super Contador')

contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')
inicioPersonalizado = int(input('Início: '))
fimPersonalizado = int(input('Fim: '))
passoPersonalizado = int(input('Passo: '))
contador(inicioPersonalizado, fimPersonalizado, passoPersonalizado)