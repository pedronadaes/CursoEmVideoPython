nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome é {} e tem {} letras.'.format(nome.find(' ')))
pnome = nome.split()
print('Seu primenrio nome é {} e ele tem {} letras'.format(pnome[0], len(pnome[0])))
