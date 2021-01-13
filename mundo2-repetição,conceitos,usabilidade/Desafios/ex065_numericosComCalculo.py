'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
print('-'*30)
print('Classificação de Números')
print('-'*30)
resposta = 'S'
soma = contador = media = maior = menor = 0
while resposta in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / contador
print('Você digitou {} números e a média deles foi {:.2f}\nO menor número digitado foi {} e o maior número foi {}'.format(contador, media, menor, maior))
print('-'*30)
print('FIM')
print('-'*30)