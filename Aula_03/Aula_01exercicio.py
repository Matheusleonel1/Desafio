# Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7

# Entrada dos Dados
altura = float(input('informe a sua altura em metros:'))
Sexo = input("Informe o sexo")

# Processamento dos Dados

if Sexo == "masculino":
    h = (72.7*altura) - 58
    print("Você é do sexo masculino")
else:
    m = (62.1*altura) - 44.7
    print("Você é do sexo feminino")

# Saida dos Dados

