# 2- Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 130,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.
print("\nObservação")
print(" Pra que a contagem seja feita de forma correta, será nescessario que informe apenas o número correspondente.")
print(" Por ex: Se a área desejada tiver 100^2 ou seja, 100 metros quadrados insira apenas o número 100")

m2 = float(input("Informe o tamanho em metros quadrados da área que deseja pintar"))
quantidade_tinta =  m2/3
litros= 1
cada_lata = litros * 18 
valor_lata = 130



print(f"A quantidade de tinta que serrá usada é {quantidade_tinta:.2f} litros")
