# 1- Faça um programa que pergunte quanto um funcionário recebe por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# a) salário bruto.
# b) Quanto pagou ao IRRF.
# c) quanto pagou ao INSS.
# d) quanto pagou ao sindicato.
# e) o salário líquido.

# Entrada de dados
salario_por_hr= float(input("Informe o valor recebido por hora trabalhada"))
horas_trabalhadas= float(input("Informe as quantidade de horas trabalhadas no mês"))

# Processamento de dados

salario_bruto = salario_por_hr * horas_trabalhadas
juros_irrf = salario_bruto*(11/100)
juros_inss = salario_bruto*(8/100)
juros_sind = salario_bruto*(5/100)
salario_liquido = salario_bruto - juros_inss - juros_irrf - juros_sind


# Saida de dados
print("\nSalario bruto")
print(f" O seu salario bruto neste mês foi de:R$ {salario_bruto:.2f}")
print(f" O valor pago ao IRRF foi de: {juros_irrf:.2f}  ") 
print(f" O valor pago ao INSS foi de: {juros_inss:.2f}  ") 
print(f" O valor pago ao sindicato foi de: {juros_sind:.2f}  ") 
print(f" O liquido recebido neste mês foi de:R$ {salario_liquido:.2f}  ") 