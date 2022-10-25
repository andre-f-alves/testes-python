try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('Não é possível a divisão por 0(zero).')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Até a próxima!')
