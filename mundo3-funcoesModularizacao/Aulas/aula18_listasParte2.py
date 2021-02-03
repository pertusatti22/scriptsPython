pessoas = [['pedro',25], ['maria',19],['joao',32]]
print(pessoas[0][0])
print(pessoas[2][1])

for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade.')

teste = list()
teste.append('Jackson')
teste.append(29)
galera = list()
galera.append(teste[:])#o simbolo [:] cria uma copia na lista
teste[0] = 'Taiana'
teste[1] = 27
galera.append(teste[:])
print(galera)

turma = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    turma.append(dado[:])
    dado.clear()
print(turma)