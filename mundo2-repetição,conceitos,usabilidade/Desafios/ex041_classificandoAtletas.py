# MÓDULOS
from datetime import date
# INICIALIZAÇÃO
print('-='*20)
print('Programa de Categorização de Atletas')
print('-='*20)
# CONFIG
nome = (str(input('Informe o nome do atleta: ')))
categorias = ['MIRIM', 'INFANTIL', 'JUNIOR', 'SÊNIOR', 'MASTER']
ano = int(input('Informe o ano de nascimento do atleta {}: '.format(nome.capitalize())))
data = date.today().year

# MOTOR DE CLASSIFICAÇÃO
if data - ano <= 9:
    print('O atleta {} foi classificado na categoria {}'.format(nome.capitalize(),categorias[0]))
elif data - ano <=14:
    print('O atleta {} foi classificado na categoria {}'.format(nome.capitalize(),categorias[1]))
elif data - ano <=19:
    print('O atleta {} foi classificado na categoria {}'.format(nome.capitalize(),categorias[2]))
elif data - ano <=20:
    print('O atleta {} foi classificado na categoria {}'.format(nome.capitalize(),categorias[3]))
else:
    print('O atleta {} foi classificado na categoria {}'.format(nome.capitalize(),categorias[4]))
print('-='*20)
print('Fim do Programa')
print('-='*20)