'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
valoresNumericos = []
while True:
    valoresNumericos.append((int(input('Digite um valor: '))))
    saida = str(input('Quer continuar? [S/N]')).upper().strip()
    if saida not in 'S':
        break
print('-='*40)
print(f'A) {len(valoresNumericos)} elementos')
valoresNumericos.sort(reverse = True)
print(f'B) {valoresNumericos}')
if 5 not in valoresNumericos:
    print('C) O valor 5 não foi encontrado na lista!')
else:
    print('C) O valor 5 foi encontrado na lista.')