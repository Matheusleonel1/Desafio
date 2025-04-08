# 5- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
# - sexo (masculino e feminino)
# - cor dos olhos (azuis, verdes ou castanhos)
# - cor dos cabelos (louros, castanhos, pretos)
# - idade
# Faça um programa que determine e escreva:
# a) a maior idade dos habitantes;
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;


# Entrada dos dados


lista_idade = []
femininas_18_35 = 0
olhos_cor = 0

quantidade_pessoas = int(input("Quantas pessoas serão analisadas? "))

for i in range(quantidade_pessoas):
    print(f"\nPessoa {i + 1}:")
    
    sexo = input("Informe o seu gênero (M/F): ").strip().upper()
    olhos = input("Informe a cor dos olhos (azuis, verdes ou castanhos): ").strip().lower()
    cabelos = input("Informe a cor dos cabelos (louros, castanhos ou pretos): ").strip().lower()
    idade = int(input("Informe a idade: "))
    
   
    # Processamento dos dados
    
    
    lista_idade.append(idade)

    if sexo == 'F' and 18 <= idade <= 35:
        femininas_18_35 += 1

    if olhos == 'verdes' and cabelos == 'louros':
        olhos_cor += 1


# Saida dos dados


maior = max(lista_idade)

print("\n--- RESULTADOS ---")
print("Lista de idades:", lista_idade)
print(f"A maior idade é: {maior}")
print(f"Quantidade de mulheres entre 18 e 35 anos: {femininas_18_35}")
print(f"Pessoas com olhos verdes e cabelos louros: {olhos_cor}")
