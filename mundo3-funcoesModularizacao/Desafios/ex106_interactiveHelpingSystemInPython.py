'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
 ‘FIM’, o programa se encerrará. Importante: use cores.'''
c = ('\033[m',          #0 sem cores
     '\033[0;30;41 m'   #1 vermelho
    );

def ajuda(com):
    help(com)

def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')

 
#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)