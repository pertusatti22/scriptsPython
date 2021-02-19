import pandas

csv_path='scriptsPython\ordens.csv'

dataFrame = pandas.read_csv(csv_path)

print(dataFrame.head())

novasColunas = {'Ativo':['Renda Fixa', 'Ações', 'Derivativos'], 'Quantidade':[1, 100, 1000], 'PreçoCompra':[10, 20, 30], 'PreçoVenda':[20, 30, 40]}

novasColunasFrame = pandas.DataFrame(novasColunas)

print(novasColunasFrame)

novaSozinha = novasColunasFrame[['Ativo']]

print(novaSozinha)
print('Fim da análise')

x = novasColunasFrame.iloc[1,0]
print(x)

'''loc is primarily label based; when two arguments are used,
you use column headers and row indexes to select the data you want. 
loc can also take an integer as a row or column number.

iloc is integer-based. You use column numbers and row numbers
 to get rows or columns at particular positions in the data frame. 

By default, ix looks for a label. If ix doesn't find a label, it will use an integer.
This means you can select data by using either column numbers and row numbers or 
column headers and row names using ix.
'''