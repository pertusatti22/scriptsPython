'''Exercício Python 73: Crie uma tupla preenchida 
com os 20 primeiros colocados da Tabela do Campeonato 
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Grêmio.'''
print('Brasileirão Séria A 2021')
serieA=('São Paulo', 'Atlético-MG', 'Internacional' ,'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Bragantino', 'Sport', 'Bahia', 'Vasco', 'Fortaleza', 'Goiás', 'Coritiba', 'Botafogo')
print('-='*40)
print(f'Lista de times do Brasileirão: {serieA}')
print('-='*40)
print(f'Os 5 primeiros são {serieA[0:5]}')
print('-='*40)
print(f'Os 4 últimos são {serieA[-4:]}')
print('-='*40)
print(f'Os times em ordem alfabética: {sorted(serieA)}')
print('-='*40)
print(f'O {serieA[serieA.index("Grêmio")]} está na {serieA.index("Grêmio")+1}º posição')
print('FIM DO PROGRAMA!')