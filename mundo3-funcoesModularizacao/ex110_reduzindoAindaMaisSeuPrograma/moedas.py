def aumentar(preço, taxa, formato = False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço, taxa, formato = False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço, formato = False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço, formato = False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço = 0, taxaAumento = 10, taxaRedução = 5):
    print('-'*33)
    print('RESUMO DO VALOR'.center(33))
    print('-'*33)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaAumento}% de aumento: \t{aumentar(preço, taxaAumento, True)}')
    print(f'{taxaRedução}% de redução: \t{diminuir(preço, taxaRedução, True)}')
    print('-'*33)