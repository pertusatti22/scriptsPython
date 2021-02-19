'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções 
incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um 
programa que importe esse módulo e use algumas dessas funções.
'''
import moedas

p = float(input('Digite o preço:'))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos {moedas.diminuir(p, 10)}')