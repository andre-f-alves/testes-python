teste = list()
teste.append('Gustavo')
teste.append(40)
manos = list()
manos.append(teste[:])
teste[0] = 'André'
teste[1] = 15
manos.append(teste[:])
print(manos)
