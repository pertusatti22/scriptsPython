'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
numeros = []
for c in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
    c += 1
print(f'O maior valor digitado foi {max(numeros)} nas posições', end=' ')
for p in range (0,5):
    if numeros[p] == max(numeros):
        posicao = numeros.index(max(numeros),p)
        print(f'{posicao}...',end = ' ')
        p +=1
print(f'\nO menor valor digitado foi {min(numeros)} nas posições', end=' ')
for p in range (0,5):
    if numeros[p] == min(numeros):
        posicao = numeros.index(min(numeros),p)
        print(f'{posicao}...',end = ' ')
        p +=1