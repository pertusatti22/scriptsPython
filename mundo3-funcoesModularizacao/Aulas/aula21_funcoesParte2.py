'''Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais 
dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''
'''from time import sleep
#escopo de variaveis com a funcao teste
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
#parametro opcional na funcao somar
def somar(a=0, b=0, c= 0):
    """
    -> Faz a soma de três valores e mostra o resultado na tea.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')
#docstring pra documetar a funcao contador
def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela.
    :param inicio: Número em que a contagem é iniciada.
    :param fim: Número em que a contagem é finalizada.
    :param passo: Número que define a cadência da contagem.
    :return: sem retorno.
    Função criada escrita por Jackson Pertusatti durante o curso em vídeo de python.
    """
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        print('Você inseriu um passo inválido!')
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='', flush = False)
            sleep(0.2)
            c += passo
        print('FIM!')
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='', flush = False)
            sleep(0.2)
            c -= passo
        print('FIM!')

def somarRetorno(a=0, b=0, c= 0):
    """
    -> Faz a soma de três valores e retorna para a variavel, 
    assim conseguimos acumular resultados de multiplas funcoes.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    """
    s = a + b + c
    return s

help(contador)
help(somar)

somar(1, 2, 3)

#escopo de variaveis
n = 2 #escopo global
print(f'No código principal, n vale {n}')
teste()
print(f'No cógigo principal, x vai dar erro, porque ela tem escopo local.')
#aqui x assume valor global
for x in range(0, 9):
    print(x)
    x += 1

r1 = somarRetorno(3,2,5)
r2 = somarRetorno(2,2)
r3 = somarRetorno(6)

print(f'Os resultados foram {r1}, {r2} e {r3} e o total é {r1+r2+r3}')'''

#parte prática
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É impar!')