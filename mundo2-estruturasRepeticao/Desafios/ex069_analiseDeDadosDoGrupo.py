'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

maioridade = masculinos = femininosVinte = 0
idade = 200
sexo = final = ' '
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    while idade not in range(0,130):
        idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        maioridade += 1 
    if sexo in 'M':
        masculinos += 1
    if idade < 20 and sexo in 'F':
        femininosVinte += 1
    print('-' * 20)
    while final not in 'SN':
        final = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 20)
    if final == 'S':
        idade = 200
        final = sexo = ' '
    else:
        print('Finalização!')
        print(f'você tem {maioridade} pessoas com mais de 18 anos. {masculinos} homens. {femininosVinte} mulheres com menos de 20 anos.')
        break
print('-' * 20)    
print('FIM DO PROGRAMA')
print('-' * 20)