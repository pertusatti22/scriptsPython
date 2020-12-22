from random import choice
primeiroAluno = str(input('Primeiro Aluno: '))
segundoAluno = str(input('Segundo Aluno: '))
terceiroAluno = str(input('Terceiro Aluno: '))
quartoAluno = str(input('Quarto Aluno: '))
lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))