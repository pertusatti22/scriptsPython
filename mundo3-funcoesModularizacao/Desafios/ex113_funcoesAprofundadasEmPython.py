'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário não inseriu dados.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário não inseriu dados.')
            return 0
        else:
            return n


num = leiaInt('Digite um valor inteiro: ')
numReal = leiaFloat('Digite um valor real: ')
print(f'O primeiro valor foi {num}, o segundo valor foi {numReal}')