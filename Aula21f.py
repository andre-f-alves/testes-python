def Par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if Par(num):
    print('O número é par!')
else:
    print('O número não é par!')
