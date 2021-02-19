'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e 
mostre a área do terreno.'''
def tituloPrograma(titulo):
    print('-' * 30)
    print(titulo)
    print('-' * 30)

def área(l, c):
    a = l * c
    print(f'A área do Terreno é de {a:.2f} m².')


#PROGRAMA PRINCIPAL
tituloPrograma('    Cálculo de m² Terrenos')
largura = float(input('Insira a Largura do Terreno: '))
comprimento = float(input('Insira o Comprimento do Terreno: '))
área(largura, comprimento)