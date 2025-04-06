# 4- Crie um programa que:
# 1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
# 2- Exiba a lista completa.
# 3- Exiba o maior e o menor número da lista
# 4- Exiba a soma e a média de todos os números.

# Entrada dos dados
numeros = []
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

# Processamento de dados 
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / len(numeros)


#Saida de dados
print("\nLista completa dos números:")
print(numeros)
print(f"\nMaior número: {maior}")
print(f"Menor número: {menor}")
print(f"\nSoma dos números: {soma}")
print(f"Média dos números: {media:.2f}")
