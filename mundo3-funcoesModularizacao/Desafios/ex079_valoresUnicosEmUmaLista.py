'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
valoresNumericos = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valoresNumericos:
        valoresNumericos.append(valor)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado! Não vou adicionar...')
    saida = str(input('Quer continuar? [S/N]')).upper().strip()
    if saida not in 'S':
        break
print('-='*40)
valoresNumericos.sort()
print(valoresNumericos)