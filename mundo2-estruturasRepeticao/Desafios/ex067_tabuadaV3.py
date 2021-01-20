'''Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo. '''
print('-='*20)
print('Tabuada V 3.0')
print('-='*20)
numero = 0
while True:
    numero = int(input('Insira um valor: '))
    if numero < 0:
        break
    else:
        print('Sua tabuada é: ')
        for n in range (1, 11):
            print (f'{n} * {numero} = {n*numero}')
print('-='*20)
print('Fim do Programa')
print('-='*20)