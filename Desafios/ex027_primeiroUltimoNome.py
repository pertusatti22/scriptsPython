nomeCompleto = str(input('Digite seu nome Completo: ')).lower().strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomeCompleto[0].capitalize()))
print('Seu último nome é {}'.format(nomeCompleto[len(nomeCompleto)-1].capitalize()))