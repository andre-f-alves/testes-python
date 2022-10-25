cores = {'limpa': '\033[m', 'azul': '\033[34m', 'vermelho': '\033[31m', 'verde': '\033[32m'}
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
print('A soma entre {}{}{} e {}{}{} é: {}{}{}.'.format(cores['azul'], n1, cores['limpa'], cores['verde'], n2, cores['limpa'], cores['vermelho'], soma, cores['limpa']))
