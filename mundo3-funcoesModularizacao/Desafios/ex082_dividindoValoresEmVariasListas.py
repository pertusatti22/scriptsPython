'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
numero = list()
par = list()
impar = list()
while True:
    numero.append(int(input('Digite um número: ')))
    saida = str(input('Quer continuar? [S/N]')).upper().strip()
    if saida not in 'S':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v) 
print('-='*40)
print(numero)
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')