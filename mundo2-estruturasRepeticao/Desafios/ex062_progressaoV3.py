'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
print('-='*20)
print('Progressão Aritmética V3')
print('-='*20)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroTermo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('-='*20)
print('Fim do Programa')
print('-='*20)