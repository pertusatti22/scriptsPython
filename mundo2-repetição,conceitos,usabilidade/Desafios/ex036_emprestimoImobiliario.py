valorCasa = float(input('Informe o preço da casa: '))
salario = float(input('Informe sua renda mensal: ')) 
prazoPagamento = float(input('Informe em quantos anos quer pagar a casa: '))
mensalidade = valorCasa/(prazoPagamento*12)
if mensalidade <= salario*0.30:
    print('Parabéns! Sua parcela é de R${:.2f}'.format(mensalidade))
else:
    print('Dinheiro negado!')