lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[0:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
#lembrete: tuplas são imutáveis.
for comida in lanche:
    print(f'Eu vou comer {comida}')
for cont in range(0, len(lanche)):
    print(f'Comendo {lanche[cont]}, na ordem {cont}')
for pos, comida in enumerate(lanche):
    print(f'Já comi {comida} na seguinte ordem: {pos}')
#ordenando alfabeticamente uma tupla
print(sorted(lanche))    
print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b+a
print(c)
print(c.count(5))
print(c.index(8))
print(c.index(2))
print(c.index(2, 4))
print(c.index(5, 1))
pessoa = ('Jackson', 29, 'M', 90)
print (pessoa)
#a tupla pode ser deletada inteira.
#del (pessoa)