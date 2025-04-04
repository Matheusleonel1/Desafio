# Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final mostre a soma e a média das idades.

# Entrada dos dados 
soma = 0
menor_idade = 100 

# Processamento dos dados - Estrutura de Repetição 
for i in range(3):
    name = input('Informe o nome do usuário:')
    idade = int(input(" Informe a idade do usuário"))
    if idade < menor_idade:
        menor_idade = idade
        maior_nome = name
   

    soma = soma = idade

print(f' A soma das idade foi {soma}') 
print(f' A média das idades foi {(soma/ (i+1)):.2f}')    
print(f'Sr(a) {maior_nome}, voce possui {maior_idade} anos, sendo a pessoa mais velha deste grupo')