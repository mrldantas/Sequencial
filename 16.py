# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = int(input("Insira o valor da área em metros quadrados: "))

litrosNecessarios = round(area / 3)
latasNececessarias = round(litrosNecessarios / 18)
preco = latasNececessarias * 80

print(f"Serão necessárias {latasNececessarias} e o valor é de: {preco}")
