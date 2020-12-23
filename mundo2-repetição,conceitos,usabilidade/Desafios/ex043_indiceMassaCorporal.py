print('-='*20)
print('Índice de Massa Corporal')
print('-='*20)
peso = float(input('Insira o seu peso em quilogramas: '))
altura = float(input('Insira a sua altura em metros: '))
imc = peso/altura/altura
if imc < 18.5:
    print('IMC: {:.2f}. Você está abaixo do peso adequado!'.format(imc))
elif imc >=18.5 and imc < 25:
    print('IMC: {:.2f}. Você está no peso ideal!'.format(imc))
elif imc >=25 and imc < 30:
    print('IMC: {:.2f}. Você está com sobrepeso!'.format(imc))
elif imc >=30 and imc < 40:
    print('IMC: {:.2f}. Você está com obesidade!'.format(imc))
else:
    print('IMC: {:.2f}. Você está com obesidade mórbida!'.format(imc))
print('-='*20)
print('Fim do Programa')
print('-='*20)