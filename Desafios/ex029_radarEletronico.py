velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Diriga com segurança!')