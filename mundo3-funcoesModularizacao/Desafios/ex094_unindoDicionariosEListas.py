'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
baseDeDados = list()
cadastroPessoas = dict()
somaDasIdades = 0
while True:   
    cadastroPessoas.clear()
    cadastroPessoas['nome'] = str(input('Nome: '))
    while True:
        cadastroPessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if cadastroPessoas['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    cadastroPessoas['idade'] = int(input('Idade: '))
    baseDeDados.append(cadastroPessoas.copy())
    somaDasIdades += cadastroPessoas['idade']
    while True:
        resposta = str(input('Quer continuar? [S/N]')).upper()[0]
        if resposta not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
        else:
            break
    if resposta == 'N':
        break
print('-='*30)
print('Análise dos dados: ')
print(f'A. Foram cadastradas {len(baseDeDados)} pessoas.')
print(f'B. A média de idade é de {int(somaDasIdades/len(baseDeDados))} anos')
print('C. As mulheres cadastradas foram: ', end='')
for p in baseDeDados:
    if p['sexo'] == 'F':
        print(f'{p["nome"].capitalize()}, ', end='')
print()
print('D. As pessoas com idade acima da média são: ', end='')
for p in baseDeDados:
    if p['idade'] >= (somaDasIdades/len(baseDeDados)):
        print(f'{p["nome"].capitalize()}, ', end='')
print()
print('-='*30)