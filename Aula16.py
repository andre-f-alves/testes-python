lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Sorvete')

print(lanche[:3])

for comida in lanche:
    print(f'Vou comer {comida}')

print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print('Enchi o pandulho!')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.index(8))
