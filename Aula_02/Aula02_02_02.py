# Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7

# Entrada dos Dados
altura = float(input('informe a sua altura em metros:'))


# Processamento dos Dados

h = (72.7*altura) - 58
m = (62.1*altura) - 44.7

# Saida dos Dados

print(f' o peso ideal para homens é {h:0f} kg.')
print (f' o peso ideal para mulheres é {m} kg.')
