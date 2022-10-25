estado = dict()
brasil = list()
for c in range(3):
    estado['estado'] = str(input('Estado: ')).strip()
    estado['sigla'] = str(input('Sigla do estado: ')).strip()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v} ', end=' ')
    print()
