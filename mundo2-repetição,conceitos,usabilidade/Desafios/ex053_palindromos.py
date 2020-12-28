'''Exercício Python 53: Crie um programa que leia uma frase qualquer 
e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
print('-='*20)
print('Identificador de Palíndromos')
print('-='*20)
frase = str(input('Insira a frase a ser testada: ')).strip().upper()
palavras = frase.split()
apoio = ''.join(palavras)
inverso = ''
#inverso = apoio[::-1]
for letra in range(len(apoio) - 1, -1, -1):
    inverso += apoio[letra]
print(apoio, inverso)
if apoio == inverso:
    print('Temos um Palíndromo!')
else:
    print('A frase não é um palíndromo!')
print('-='*20)
print('Fim do Programa')
print('-='*20)