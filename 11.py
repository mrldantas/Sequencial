import math

primeiroNumero = int(input("Insira um numero inteiro: "))
segundoNumero = int(input("Insira outro numero inteiro: "))
terceiroNumero = int(input("Insira outro numero (raiz): "))

raiz = math.sqrt(terceiroNumero)

a = "Produto do dobro do primeiro com metade do segundo"
b = "A soma do triplo do primeiro com o terceiro"
c = "O terceiro elevado ao cubo"

primeiroResultado = (primeiroNumero * 2) * (segundoNumero/2)
print(f"{a}: {primeiroResultado}")

segundoResultado = (primeiroNumero * 3) + terceiroNumero
print(f"{b}: {segundoResultado}")

terceiroResultado = terceiroNumero * terceiroNumero * terceiroNumero
print(f"{c}: {terceiroResultado}")
