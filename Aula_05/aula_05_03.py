# 2- Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem crescente

# Entrada dos dados
n = 1
qtd_par = 0
qtd_impar = 0
num = []
num_par = []
num_impar = []

# Processamento dos dados
for i in range(10):
    num.append(int(input(f'Informe o {n}o. Valor: ')))
    n += 1
    if num[i] % 2 == 0:
        qtd_par += 1
    else:
        qtd_impar += 1

# Saída dos dados
print(f'A quantidade de números pares é {qtd_par}')
print(f'A quantidade de números ímpares é {qtd_impar}')
num.reverse()
print('\nLista em Ordem Reversa')
print(num)
num.sort()
print('\nLista em Ordem Crescente')
print(num)
