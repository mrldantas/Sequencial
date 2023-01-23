# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horasGanhos = int(input("Insira quanto você ganha por hora: "))
horasTrabalhadas = int(input("Insira quantas horas você trabalhou esse mês: "))

salario = horasGanhos * horasTrabalhadas

print(f"Seu salário esse mês é de: {salario}")
