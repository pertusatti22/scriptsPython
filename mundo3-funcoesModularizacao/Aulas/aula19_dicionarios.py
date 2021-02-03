'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma
estrutura, acessíveis por chaves literais.'''
'''dados = dict()
dados = {'nome':'Pedro','idade':25}
lista = [dados]
dados['sexo']='M'
del dados['idade']
print(dados.values())
print(dados.keys())
print(dados.items())
print(lista[0]['sexo'])
for k, v in dados.items():
    print(f'O {k} é {v}')'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')