from random import shuffle
primeiroAluno = str(input('Primeiro Aluno: '))
segundoAluno = str(input('Segundo Aluno: '))
terceiroAluno = str(input('Terceiro Aluno: '))
quartoAluno = str(input('Quarto Aluno: '))
lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(lista)
print('A ordem da apresentação sera: ')
print(lista)