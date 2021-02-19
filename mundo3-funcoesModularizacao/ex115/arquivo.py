import interface

def arquivoExiste(nome):
    try:
        a = open('D:\Arquivos de Programas\Xampp\htdocs\meusAplicativos\scriptsPython\mundo3-funcoesModularizacao\ex115\\'+nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open('D:\Arquivos de Programas\Xampp\htdocs\meusAplicativos\scriptsPython\mundo3-funcoesModularizacao\ex115\\'+nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso\033[m')


def lerArquivo(nome):
    try:
        a = open('D:\Arquivos de Programas\Xampp\htdocs\meusAplicativos\scriptsPython\mundo3-funcoesModularizacao\ex115\\'+nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open('D:\Arquivos de Programas\Xampp\htdocs\meusAplicativos\scriptsPython\mundo3-funcoesModularizacao\ex115\\'+arq, 'at')
    except:
        print('\033[31mErro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mErro ao escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()