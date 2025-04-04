# Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E.

GABARITO = ['A','B','B','D','E']

prova=[]

acerto =0
erro = 0

n=1

for i in range (5): 
    prova.append(input(f"Informe a alternativa marcada{n}"))
    n += 1


for i in range(len(prova)):
    if prova [i].upper() == GABARITO[i]:
        acerto +=1
    else:
        erro+=1    

# Saida dos dados

print('\n As alternativas informadas foram')    
print(prova)

print('\n As alternativas corretas foram')    
print(GABARITO)

print(f"Portanto você acertou {acerto} questões ")