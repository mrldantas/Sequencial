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
