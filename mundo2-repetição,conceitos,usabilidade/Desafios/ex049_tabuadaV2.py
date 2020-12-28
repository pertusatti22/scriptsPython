'''Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada 
de um número que o usuário escolher, só que agora utilizando um laço for.'''
print('-='*20)
print('Tabuada V 2.0')
print('-='*20)
#Somatório
numero = int(input('Insira um valor: '))
print('Sua tabuada é: ')
for n in range (1, 11):
    print ('{} * {} = {}'.format(n, numero, n*numero))
print('-='*20)
print('Fim do Programa')
print('-='*20)