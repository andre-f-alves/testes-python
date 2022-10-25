n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
print('A \033[1;36msoma\033[m entre \033[33m{}\033[m e \033[35m{}\033[m é: \033[4;34m{}\033[m'.format(n1, n2, soma))
nome = str(input('Qual o seu nome? ')).strip()
print('Olá {}{}{}! Seja bem vindo!'.format('\033[4;32m', nome, '\033[m'))
