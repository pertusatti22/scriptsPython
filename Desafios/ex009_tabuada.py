numero = int(input('Insira um valor: '))

print('Sua tabuada é: ')
for n in range (1, 11):
    tabuada = n * numero
    print ('{} * {} = {}'.format(n, numero, tabuada))