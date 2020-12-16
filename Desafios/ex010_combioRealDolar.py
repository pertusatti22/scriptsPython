#considerar 1 dólar = 3,27 reais

dinheiro = float(input('Insira o valor que deseja converter: '))
cambio = 3.27

resultado = (dinheiro/cambio)

print('Você pode comprar {:.2f} dólares com {:.2f} reais.'.format(resultado, dinheiro))