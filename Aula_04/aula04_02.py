# 1- Escreva um programa que, dado 5 números inteiros calcule a soma deles e identifique o maior deles.

# Entrada dos dados
soma = 0
Maior = 0

# Processamento de dados - Estrutura de Repetição
for i in range(5):
    n = int(input('Informe um valor interiro'))
    if n > Maior:
        Maior =  n
    soma = soma + n

# Saida de dados
print(f'a soma é {soma}')    
    

