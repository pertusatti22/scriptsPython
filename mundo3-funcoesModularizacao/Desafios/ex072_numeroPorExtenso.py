'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
print('Números por Extenso')
numeroExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: [999 para sair]'))
    if 0<= numero <=20:
        print(f'Você digitou o número {numeroExtenso[numero]}')
    if numero == 999:
        break
print('Fim do Programa!')