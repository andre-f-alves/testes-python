try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('ERRO!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Até a próxima!')
