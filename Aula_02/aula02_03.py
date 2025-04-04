# Escreva um programa que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula: 
# valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

# Entrada dos dados
Prestacao = float(input('informe o valor da prestação:'))
taxa = float(input('informe a taxa em percentual:'))
tempo = int(input('informe o atraso em dias:'))

# Processamento dos Dados

juros = Prestacao*(taxa/100)*tempo
valorfinal = Prestacao + juros

#Saida dos Dados

print(f' A prestação se encontra {tempo} dias atrasada, gerando um juros de R$ {juros:.2f}, portanto o valor final a ser pago será de R${valorfinal:,.2f}') 
