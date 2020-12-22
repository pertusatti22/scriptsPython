preco = float(input('Qual o valor da casa: '))
renda = float(input('Qual é o valor do seu salário: '))
prazo = float(input('Qual o prazo (anos) de pagamento almejado: ')

#calcular prestação mensal, que não pode exceder 30% do salário, caso exceda, empréstimo negado.

if mensalidade < renda*0.3:
    print ('Empréstimo aprovado, sua prestação mensal ficou em R${:.2f}'.format(mensalidade)
else:
    print ('Seu empréstimo foi Negado!')