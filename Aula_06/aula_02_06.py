# 2- Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.


import math
# Orientaçoes
print("\nObservação")
print(" Para que a contagem seja feita de forma correta, será necessário informar apenas o número correspondente..")
print(" Por exemplo: se a área desejada for de 100 metros quadrados (100 m²), insira apenas o número 100")

# Entrada de dados
m2 = float(input("Informe o tamanho em metros quadrados da área que deseja pintar")) # m2 = mestros quadrados

# Processamento de dados
quantidade_tinta =  m2/3
latas = 18  # litros
quantidade_latas = math.ceil(quantidade_tinta / latas)
valor_compra = quantidade_latas * 130.00


# Saida dos dados
print(f"A quantidade de tinta que será usada é {quantidade_tinta:.2f} litros")
print(f"A quantidade de latas nescessarias que serão usadas é {quantidade_latas:.2f}")
print(f"O valor final de sua compra é de: {valor_compra:.2f} reais")

