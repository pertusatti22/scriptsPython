nota1 = float(input('Insira a Primeira nota: '))
nota2 = float(input('Insira a Segunda nota: '))
materias = [nota1,nota2]

media = float((nota1+nota2)/len(materias))

print('A partir das notas informadas, a média do aluno é: {}'.format(media))