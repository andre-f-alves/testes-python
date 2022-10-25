galera = list()
dados = list()
maior = menor = 0
for c in range(3):
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'{maior} pessoas são maiores de idade e {menor} são menores de idade.')
