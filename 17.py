# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;

area = int(input("Insira o valor da área em metros quadrados: "))

litrosNecessarios = (area / 6)
latasNecessarias = (litrosNecessarios / 18)
galoesNecessarios = (litrosNecessarios / 3.6)
precoLata = latasNecessarias * 80
precoGalao = galoesNecessarios * 25

a = "Se for apenas latas serão necessárias"
b = "Se for apenas galões serão necessários"

print(f"{a} {round(latasNecessarias)} com o valor de {round(precoLata)}")
print("ou")
print(f"{b} {round(galoesNecessarios)} com o valor de {round(precoGalao)}")
