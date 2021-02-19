#Módulos e Bibliotecas
import interface
import arquivo
import colorama
colorama.init()
from time import sleep

#Banco de Dados
arq = 'database.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

#Programa Principal
while True:
    resposta = interface.menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        interface.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 2:
        arquivo.lerArquivo(arq)
    elif resposta == 3:
        print('Saindo do sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.2)