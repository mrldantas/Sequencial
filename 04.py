# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

primeiraNota = float(input("Insira a nota do primeiro bimestre: "))
segundaNota = float(input("Insira a nota do segundo bimestre: "))
terceiraNota = float(input("Insira a nota do terceiro bimestre: "))
quartaNota = float(input("Insira a nota do quarto bimestre: "))

bimestres = 4

primeiraMetade = primeiraNota + segundaNota
segundaMetade = terceiraNota + quartaNota

print(f"A média é: {round((primeiraMetade + segundaMetade)/bimestres)}")
