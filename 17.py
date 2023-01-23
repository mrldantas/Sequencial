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
