print('-='*20)
print('Clássico das Médias de Notas')
print('-='*20)
nota1 = float(input('informe sua primeira nota: '))
nota2 = float(input('informe sua segunda nota: '))
resultado = (nota1 + nota2)/2
if resultado < 5:
    print('REPROVADO')
elif resultado >= 5 and resultado <= 6.9:
    print('RECUPERAÇÃO')
elif resultado >= 7 and resultado <= 10:
    print('APROVADO')
else:
    print('Você inseriu notas erradas!')
print('-='*20)
print('Fim do Programa')
print('-='*20)