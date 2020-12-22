print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos acima PODEM FORMAR triângulos!')
else:
    print('Os elementos acima NÃO PODEM FORMAR triângulos!')