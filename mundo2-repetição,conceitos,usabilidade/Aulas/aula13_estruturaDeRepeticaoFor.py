'''for c in range(1, 7,-1):
    print(c)
for c in range(1, 7,-1):
    print(c)    
for c in range(1, 7, 2):
    print(c)    
print ('FIM')'''
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')