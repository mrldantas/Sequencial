# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

horasTrabalhadas = int(input("Insira quantas horas você trabalhou esse mês: "))
horasGanho = int(input("Insira quanto você ganha por hora trabalhada: "))

salarioBruto = horasTrabalhadas * horasGanho
impostoRenda = salarioBruto * 0.11
sindicato = salarioBruto * 0.05
inss = salarioBruto * 0.08
salarioLiquido = salarioBruto - impostoRenda - sindicato - inss

print(f"Salário bruto: R${salarioBruto}")
print(f"Imposto de Renda: R${impostoRenda}")
print(f"INSS: R${inss}")
print(f"Sindicato: R${sindicato}")
print(f"Salário Líquido: R${salarioLiquido}")
