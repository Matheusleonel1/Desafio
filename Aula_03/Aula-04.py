# 1- Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições: 

# • Ter entre 16 e 69 anos.
# • Pesar mais de 50 kg.
# • Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)


# Entrada de dados

idade = int(input("Informe a idade"))
Peso = float(input("informe o peso" ))
Horas_sono = float(input("informe as horas de sono"))

# Processamento de dados

if idade >= 16:
    print("Você atende os requisitos de doação")
else:
    
     print("Você não atende os requisitos de doação") 

if idade <= 56:
    print("Você atende os requisitos de doação")
else:
    print("Você não atende os requisitos de doação")  
if idade < 16:
    print("Você não atende os requisitos de doação pois a idade é menor do que a permitida")

if idade > 56:
    print("Você não atende os requisitos de doação pois a idade é maior do que a permitida")
else:
    print("Você não atende os requisitos de doação")          

if Peso < 50:
    print("Você não atende os requisitos de doação pois o peso é menor do que a permitida")

else:
     print("Parabésns você atende os requisitos de doação pois pois está no peso adequado")   


if Horas_sono < 6:
    print("Você não atende os requisitos de doação pois o tempo de sono é menor do que a permitida")

else:
   print("Parabésns você atende os requisitos de doação pois pois manteve as horas de sono adequadas") 

