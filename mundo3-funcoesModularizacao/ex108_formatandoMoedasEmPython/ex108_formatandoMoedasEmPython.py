'''
Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga
mostrar os números como um valor monetário formatado.
'''
import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de R$ {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de R$ {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'Diminuindo 10%, temos {moedas.moeda(moedas.diminuir(p, 10))}')