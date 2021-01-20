'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
e quantas mulheres têm menos de 20 anos.'''
from statistics import mean
print('-='*20)
print('Analisador Completo de Perfil')
print('-='*20)
idadeLista = []
homemVelho = 0
nomeVelho = ''
mulherMenor = 0
for c in range(1, 5):
    print('---- {}ª Pessoa ----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idadeLista.append(idade)
    if c == 1 and sexo in 'Mm':
        homemVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > homemVelho:
        homemVelho = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade <= 20:
        mulherMenor += 1
print('A média de idade do grupo é de {:.1f} anos'.format(mean(idadeLista)))
print('O homem mais velho tem {} anos e se chama {}.'.format(homemVelho,nomeVelho.capitalize()))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulherMenor))
print('-='*20)
print('Fim do Programa')
print('-='*20)