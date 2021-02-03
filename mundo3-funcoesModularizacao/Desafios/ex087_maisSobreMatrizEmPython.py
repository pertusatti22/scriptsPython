'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
bValor = 0
aValor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            aValor += matriz[l][c]
    bValor += matriz[l][2]
    cValor = max(matriz[1])
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {aValor}')
print(f'A soma dos valores da terceira coluna é {bValor}')
print(f'O maior valor da segunda linha é {cValor}.')