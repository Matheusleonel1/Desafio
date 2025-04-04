# Programa Média

# Entrada de Deados
nome = input('informe nome do estudante: ')
n1 = float(input('informe a primeira nota{nome}:'))
n2 = float(input('informe a segunda nota{nome}:'))
n3 = float(input('informe a terceira nota:{nome}'))

# Processamento dos dados
media = (n1+n2+n3)/3


# Saida dos Dados
print(f'Sr(a) {nome}, a sua média foi { media: .1f} ')
