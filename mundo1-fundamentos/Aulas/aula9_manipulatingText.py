'''tecnicas de tratamento de strings
FATIAMENTO
frase[3:9] frase [2:] frase [:5] frase[4:9:2]
analise de string
len(frase) = length
frase.count('o') frase.count('o', 0, 13)
frase.find('deo') = indica onde o trecho '' começa, posição na string.
boolean 'Curso" in frase >>> true
frase.upper() >>> uppercase
frase.lower() >>> lowercase
frase.title() >>> Capitalyze
frase.strip() >>> remove os espaços inúteis no início e final das strings.
frase.rstrip() >>> r de right, remove apenas os espaços na direita.
frase.lstrip() >>> l de left, remove apenas os espaços na esquerda.
DIVISÃO DE STRINGS
frase.split() >>> vai dividir a string conforme os espaços 
entre as palavras, criando novas strings.
JUNÇÃO DE STRINGS
'-'.join(frase)
'''
#EXERCÍCIOS EM SALA
frase = 'Curso em Vídeo Python'
frase2= '   Aprendendo Python  '
#Fatiamentos
print(frase[:13])
print(frase[13:])
print(frase[1:8:10])
print(frase[1:15:3])
print(frase[::3])
#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('O'))#python diferençia case sensitive
print(frase.upper().count('O'))#Posso combinar multiplos comandos
print(frase.count('e', 0, 13)) #contagem com fatiamento
print(frase.find('deo'))
print('Curso' in frase)
print(frase.upper())
print(frase.lower())
print(frase.title())
print(frase2.strip()) 
print(frase2.rstrip())
print(frase2.lstrip())
dividir = frase.split()
print(dividir)
print(dividir[1])
print(dividir[0][2])
print('-'.join(frase2))
print(frase2.replace('Python', 'Android'))

print("""Dessa forma é possível printar textos
com diversas linhas escritas no código.
Assim como estou escrevendo agora.""")