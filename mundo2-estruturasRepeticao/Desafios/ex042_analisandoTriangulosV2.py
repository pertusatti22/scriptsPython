print('-='*20)
print('Analisador de Triângulos V 2.0')
print('-='*20)
r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os elementos acima PODEM FORMAR um triângulo!')
    if r1 == r2 == r3:
        print('O triângulo formado é Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado é Isósceles')
    else:
        print('O triângulo formado é Escaleno')
else:
    print('Os elementos acima NÃO PODEM FORMAR um triângulo!')
print('-='*20)
print('Fim do Programa')
print('-='*20)