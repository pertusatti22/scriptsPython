'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
 e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
 No final, mostre a lista ordenada na tela.'''
posicaoLista = []
for c in range(0,4):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > posicaoLista[-1]:
        posicaoLista.append(valor)
    else:
        p = 0
        while p < len(posicaoLista):
            if valor <= posicaoLista[p]:
                posicaoLista.insert(p,valor)
                break
            p +=1
print(posicaoLista)