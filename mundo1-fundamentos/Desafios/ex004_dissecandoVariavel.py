#Dissecando uma variável

analise = input('Digite algo:')

print('O tipo primitivo desse valor é {}'.format(type(analise)))
print('Só tem espaços? {}'.format(analise.isspace()))
print('É um número? {}'.format(analise.isnumeric()))
print('É alfabético? {}'.format(analise.isalpha()))
print('É alfanumérico? {}'.format(analise.isalnum()))
print('Está em maiúsculas? {}'.format(analise.isupper()))
print('Está em minúsculas? {}'.format(analise.islower()))
print('Está capitalizada? {}'.format(analise.istitle()))