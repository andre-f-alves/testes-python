n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'a soma dos números é {s}')

"""# F - strings
nome = 'José'
idade = 45
print(f'{nome} tem {idade} anos.') # PYTHON 3.6+
print('{} tem {} anos'.format(nome, idade)) # PYTHON 3
print(nome, 'tem', idade, 'anos.')
print('%s tem %d anos.' % (nome, idade)) # PYTHON 2"""
