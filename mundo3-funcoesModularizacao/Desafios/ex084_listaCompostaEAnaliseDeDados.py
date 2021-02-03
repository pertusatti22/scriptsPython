'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
listaDePessoas = list()
valorIndividual = list()
maior = menor = 0
while True:
    valorIndividual.append(str(input('Nome: ')))
    valorIndividual.append(float(input('Peso: ')))
    ###Estrutura para testar maior e menor###
    if len(listaDePessoas) == 0:
        maior = menor = valorIndividual[1]
    else:
        if valorIndividual[1] > maior:
            maior = valorIndividual[1]
        if valorIndividual[1] < menor:
            menor = valorIndividual[1]
    #########################################        
    listaDePessoas.append(valorIndividual[:])
    valorIndividual.clear()
    fimDoPrograma = str(input('Quer Continuar? [S/N]')).upper().strip()
    if fimDoPrograma not in 'S':
        break
print('-='*30)
print(f'Foram cadastradas {len(listaDePessoas)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de: ',end = '')
for p in listaDePessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor} Kg. Peso de: ',end = '')
for p in listaDePessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')