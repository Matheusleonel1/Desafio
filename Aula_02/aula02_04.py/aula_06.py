# Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada.

# Entrada de dados

Consumo = 12
dm = int(input(' Informe a Distancia percorrida em (Km) :')) 
tempo = int(input(' Informe o tempo de viagem em horas:'))


#Processamento de dados

vm = dm / tempo
l = dm/Consumo

# Saida de dados

print(f' A velocidade do veiculo {vm} em Km/h')
print(f' A quantidade de combustivel utilizado foi {l:.1f}')