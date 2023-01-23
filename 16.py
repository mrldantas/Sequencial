area = int(input("Insira o valor da área em metros quadrados: "))

litrosNecessarios = round(area / 3)
latasNececessarias = round(litrosNecessarios / 18)
preco = latasNececessarias * 80

print(f"Serão necessárias {latasNececessarias} e o valor é de: {preco}")
