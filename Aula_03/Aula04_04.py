# 1- Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições: 

# • Ter entre 16 e 69 anos.
# • Pesar mais de 50 kg.
# • Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)


# Entrada de dados

idade = int(input("Informe a idade"))
Peso = float(input("informe o peso" ))
Horas_sono = float(input("informe as horas de sono"))

if idade > 16 or idade < 69:
    print("Você atende os requisitos de doação")
else:
    
    print("Você não atende os requisitos de doação")
