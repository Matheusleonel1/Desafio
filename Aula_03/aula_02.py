# 1- Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.

# Entrada de dados

n1 = int(input("Informe o primeiro valor"))
n2 = int(input("Informe o segundo valor"))


# Processamento de dados

if n1 == n2:
    print(f"Os valores são iguais, portanto a soma vale { n1 + n2} ")

else:
    print(f"Os valores são diferentes, portanto o produto vale{n1*n2}")