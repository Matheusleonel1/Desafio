# - O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas.

# entrada dos dados

temperaturas = []

quantidade = int(input("Quantas temperaturas você deseja informar? "))

for i in range(quantidade):
    temp = float(input(f"Digite a temperatura {i + 1}: "))
    temperaturas.append(temp)


# Processamento dos dados

maior = max(temperaturas)
menor = min(temperaturas)
media = sum(temperaturas) / len(temperaturas)


# Saida dos dados


print("\n--- RESULTADOS ---")
print("Temperaturas registradas:", temperaturas)
print(f"Maior temperatura: {maior} ºC")
print(f"Menor temperatura: {menor} ºC")
print(f"Média das temperaturas: {media:.2f} ºC")


