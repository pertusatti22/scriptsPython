print('-='*20)
print('Gerenciador de Condições de Pagamentos')
print('-='*20)

repetidor = False
precoDoProduto = float(input('Insira o preço do produto: R$'))
print('Agora selecione a condição de pagamento:')
while not repetidor:
    codigosPagamento = ['A','B','C','D']    
    print('Cód | Forma de Pagamento\n {}  | Dinheiro ou Débito\n {}  | à Vista no Cartão\n {}  | até 2x no Cartão\n {}  | 3 ou + vezes no Cartão'.format(codigosPagamento[0],codigosPagamento[1],codigosPagamento[2],codigosPagamento[3]))
    condicaoPagamento = str(input('Digite ao lado o código da forma de pagamento e confirme apertando "ENTER": '))
    if condicaoPagamento.lower() == 'a':
        condicaoPagamento = 0
    elif condicaoPagamento.lower() == 'b':
        condicaoPagamento = 1
    elif condicaoPagamento.lower() == 'c':
        condicaoPagamento = 2
    elif condicaoPagamento.lower() == 'd':
        condicaoPagamento = 3
    codigosPagamento = ['Dinheiro ou Débito','à Vista no Cartão','até 2x no Cartão','3 ou + vezes no Cartão']
    print('A condição de pagamento selecionada foi: {}'.format(codigosPagamento[condicaoPagamento]))
    if condicaoPagamento == 3:
        parcelador = False
        while not parcelador:
            parcelas = int(input('Selecione a quantidade de 3 até 12 parcelas, no cartão de crédito: '))
            if parcelas < 3 or parcelas > 12:
                print('Quantidade de parcelas inválida!')
                parcelador = False
            else:
                break
    confirmador = input('Confirma a condição de pagamento(s/n)? ')
    if confirmador.lower() == 's':
        break
    else:
        repetidor == False
print ('Condição de pagamento selecionada com sucesso! A condição é: {}'.format(codigosPagamento[condicaoPagamento]))
print ('O preço normal do produto é de R${:.2f}.'.format(precoDoProduto))
if condicaoPagamento == 0:  
    print('Ao pagar com {}, o preço final é de R${:.2f}'.format(codigosPagamento[condicaoPagamento],(precoDoProduto*0.9)))
elif condicaoPagamento == 1:
    print('Ao pagar com {}, o preço final é de R${:.2f}'.format(codigosPagamento[condicaoPagamento],(precoDoProduto*0.95)))
if condicaoPagamento == 2:
    print('Ao pagar com {}, o preço final é de R${:.2f}, em 2 vezes no cartão, com parcelas no valor de {:.2f}'.format(codigosPagamento[condicaoPagamento], precoDoProduto, (precoDoProduto/2)))
if condicaoPagamento == 3:
    print('Ao pagar com {}, o preço final é de R${:.2f}, em {} vezes no cartão, com parcelas no valor de {:.2f}'.format(codigosPagamento[condicaoPagamento], (precoDoProduto*1.2), parcelas, (precoDoProduto/parcelas)))
print('-='*20)
print('Fim do Programa')
print('-='*20)