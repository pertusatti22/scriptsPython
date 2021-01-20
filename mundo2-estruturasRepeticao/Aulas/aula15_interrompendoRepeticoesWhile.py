'''Nessa aula, vamos aprender como utilizar a instrução break 
e os loopings infinitos a favor das nossas estratégias de código. 
É muito importante saber usar o break no Python, já que em alguns 
casos precisamos interromper um laço no meio do caminho.
Além disso, vamos aprender como trabalhar com as novas fstrings do Python.'''
numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 000:
        break
    soma += numero
print(f'A soma vale {soma}')
#f antes da string (fstring) substitui o .format
'''exemplos:
nome = 'José'
idade = 33
salario = 987.35
print(f'O nome {nome:->20} tem {idade>-^20} anos e ganha R$ {salario:.2f}.') python3.6+'''