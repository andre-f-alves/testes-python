pessoas = {'nome': 'André', 'idade': 15, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 72.5
for c in pessoas.keys():
    print(c)
print()
for v in pessoas.values():
    print(v)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')