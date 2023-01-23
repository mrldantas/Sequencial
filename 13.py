sexo = input("Insira se você é homem ou mulher: ")

if (sexo == "Homem" or sexo == "homem"):
    altura = float(input("Insira sua altura: "))
    resultado = round((72.7 * altura) - 58)
    print(f"Seu peso ideal é: {resultado}")

if (sexo == "Mulher" or sexo == "mulher"):
    altura = float(input("Insira sua altura: "))
    resultado = round(((62.1 * altura) - 44.7))
    print(f"Seu peso ideal é: {resultado}")
