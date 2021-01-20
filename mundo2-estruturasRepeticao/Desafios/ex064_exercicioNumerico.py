'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
print('-'*30)
print('Somatório de Números')
print('-'*30)
contador = somatorio = numero = 0
numero = int(input('Digite um número [Digite 999 para parar]: '))
while numero != 999:    
    contador += 1    
    somatorio = somatorio + numero
    numero = int(input('Digite um número [Digite 999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(contador, somatorio))
print('-'*30)
print('FIM')
print('-'*30)