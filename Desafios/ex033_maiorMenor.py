primeiroValor = float(input('Primeiro Valor: '))
segundoValor = float(input('Segundo Valor: '))
terceiroValor = float(input('Terceiro Valor: '))
#menor = min(primeiroValor, segundoValor, terceiroValor)
#maior = max(primeiroValor, segundoValor, terceiroValor)
menor = primeiroValor
if segundoValor < primeiroValor and segundoValor < terceiroValor:
    menor = segundoValor
if terceiroValor < primeiroValor and terceiroValor < segundoValor:
    menor = terceiroValor
maior = primeiroValor
if segundoValor > primeiroValor and segundoValor > terceiroValor:
    maior = segundoValor
if terceiroValor > primeiroValor and terceiroValor > segundoValor:
    maior = terceiroValor
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))