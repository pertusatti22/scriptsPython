periodo = int(input('Quantos dias alugados? '))
distancia = int(input('Quantos Km rodados? '))
total = (periodo * 60) + (distancia * 0.15)

print('O total a pagar é de R${}'.format(total))