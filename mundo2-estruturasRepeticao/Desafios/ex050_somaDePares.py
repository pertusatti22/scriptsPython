'''Exercício Python 50: Desenvolva um programa que leia seis números inteiros 
e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
print('-='*20)
print('Soma dos Pares')
print('-='*20)
soma = 0
cont = 0
for d in range (1, 7):
    numero = int(input('Digite o {}º valor: '.format(d)))
    if numero % 2 == 0:
        soma = soma+numero
        cont += 1
print('A soma dos {} números pares é {}'.format(cont, soma))
print('-='*20)
print('Fim do Programa')
print('-='*20)