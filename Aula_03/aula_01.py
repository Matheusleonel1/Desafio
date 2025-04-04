idade = int(input("Informe sua Idade:"))
if idade < 18:
    print(" Você é menor de idade")
elif idade == 18:
    print("Você tem exatos 18 anos - Acesso Liberado")
elif idade >= 65:
    print("Você tem mais de 65 anos - Acesso Liberado")
else:
    print("Acesso Liberado")
