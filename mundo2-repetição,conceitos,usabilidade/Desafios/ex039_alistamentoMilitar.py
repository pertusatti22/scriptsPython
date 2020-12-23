from datetime import date
print('-='*20)
print('Programa de Alistamento Militar')
print('-='*20)
nome = (str(input('Informe seu nome: ')))
genero = (str(input('Informe seu genero: ')))
if genero.lower() == 'masculino':
    ano = int(input('Informe seu ano de nascimento, sr.{}: '.format(nome)))
    data = date.today().year
    if data - ano == 18:
        print('Sr. {}, é hora de se alistar!'.format(nome))
    elif data - ano < 18:
        print('você ainda é jovem, {}! Retorne em {} anos, para o seu alistamento.'.format(nome,(ano-(data-18))))
    else:
        print('Sr. {}, você já deveria ter se alistado há {} anos. Procure a Junta Militar mais próxima!!'.format(nome,((data-18)-ano)))
else:
    print('Você não precisa se alistar!')
print('-='*20)
print('Fim do Programa')
print('-='*20)