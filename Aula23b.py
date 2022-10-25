try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Probelma encontrado: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Até a próxima!')
