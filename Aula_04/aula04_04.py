# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:

# - Se a média for maior igual a 70 -> ATENDIDO
# - Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# - Se a média for menor que 30 -> NÃO ATENDIDO




for i in range(3):
    name = input("Informe o seu nome")
    n1 = float(input(f"Informe a primeira nota "))
    n2 = float(input("informe a segunda nota")) 

    media = (n1 + n2)/2 

    if media >= 70:
        situação = ("ATENDIDO") 
    elif media >= 30 and media < 70:
        situação = ("PARCIALMENTE ATENDIDO") 
    else:
        situação = ("NÃO ATENDIDO")    


    print(f' Sr(a){name} A sua média foi {(media):.2f}, portanto sua sitiação é: {situação} ') 

