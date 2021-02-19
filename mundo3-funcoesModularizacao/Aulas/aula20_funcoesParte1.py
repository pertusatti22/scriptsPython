'''Nessa aula, vamos aprender o que são funções ou ROTINAS
e como utilizar funções em Python. Funções são trechos de
código que podem ser executados em momentos diferentes de 
nossos códigos em Python. Veja como funciona o comando def 
em Python e como utilizá-lo com parâmetros simples e múltiplos.'''
def tituloPrograma(titulo):
    print('-' * 30)
    print(titulo)
    print('-' * 30)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(s)

def contador(* núm):
    print(f'Recebi os valores{núm} e são ao todo {len(núm)} números.')

def dobraValores(listaValores):
    pos = 0
    while pos < len(listaValores):
        listaValores[pos] *= 2
        pos += 1


tituloPrograma('   Aprendendo Funções em Python')

tituloPrograma('        Parte Prática')
soma(4, 5, 3)
soma(8, 9, 4, 50, 100)
soma(2, 1)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
dobraValores(valores)
print(valores)