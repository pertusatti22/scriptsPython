print('=-'*20)
print('Bases de Conversão')
print('=-'*20)
print('Regras:')
print('Primeiro, insira o número que deseja converter, e em seguida, ')
print('insira a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal')
numero = int(input('Digite um número: '))
baseConversao = int(input('Digite a conversão: '))
if baseConversao == 1:
    print('O número {} em binário é {}.'.format(numero, bin(numero)))
elif baseConversao == 2:
    print('O numero {} em octal é {}'.format(numero, oct(numero)))
elif baseConversao == 3:
    print('O numero {} em hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Você não selecionou a base corretamente!')
print('-='*20)
print('Fim do Programa')
print('-='*20)