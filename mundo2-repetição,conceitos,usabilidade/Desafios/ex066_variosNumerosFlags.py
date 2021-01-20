'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
print('-'*30)
print('estrutura com flag')
print('-'*30)
numero = cont = soma = 0
while True:
    numero = int(input('Digite um número (digite 0 para encerrar): '))
    if numero == 000:
        break
    soma += numero
    cont += 1
print(f'A soma dos {cont} números é igual a {soma}')
print('-'*30)
print('FIM')
print('-'*30)