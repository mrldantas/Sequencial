peso = int(input("Insira quantos quilos de peixe foi pescado: "))

pesoMaximo = 50
pesoExcesso = peso - pesoMaximo

a = "O peso máximo foi excedido, o valor da multa é:"

multa = pesoExcesso * 4

if (peso > pesoMaximo):
    print(f"{a} {multa} reais")
