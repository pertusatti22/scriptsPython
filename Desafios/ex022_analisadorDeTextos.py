nome = str(input('Digite seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
primeiroNome = nome.split()
print(len(primeiroNome[0]))

print(nome.find(' '))