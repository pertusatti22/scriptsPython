'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma
mesma estrutura, acessíveis por chaves individuais.'''
'''métodos de lista
lista.append() #insere um valor adicional no final da lista
lista.inset(0,'valor') #insere um valor na lista na posição definida
del lista[3] #deleta elemento pelo indice
lanche.pop(3) #tbm deleta elemento pelo indice
lanche.remove('valor') #remove pelo valor do elemento
valores = list(range(4,11)) #cria lista de numeros em ordem
valores = [9,3,5,6,7]
valores.sort() #organiza a lista em ordem
valores.sort(reverse=True) #organiza na ordem inversa
len(valores) #quantos valores tem a lista, começando do zero.
'''
print('EXEMPLO 01')
num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
num.sort(reverse = True)
num.insert(2,6)
print(num)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
if 1 in num:
    num.remove(1)
else:
    print('Não achei o número 1')
del num[0]
num.sort()
print(num)

print('EXEMPLO 02')
listaValores = novosValores = []
listaValores.append(5)
listaValores.append(9)
listaValores.append(4)
for c, v in enumerate(listaValores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Final da execução!')
for cont in range(0,5):
    novosValores.append(int(input('Digite um valor: ')))
print(novosValores)

print('EXEMPLO 03')
listaDeNumeros = [2,3,4,7]
b = listaDeNumeros[:]
b[2] = 8
print(f'Lista A: {listaDeNumeros}')
print(f'Lista B: {b}')