# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
# Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanhoArquivo = float(input("Insira o tamanho do arquivo em MB: "))
velocidadeInternet = int(input("Insira a velocidade da sua internet: "))

velocidadeDownload = (tamanhoArquivo)/(velocidadeInternet/8)

if (velocidadeDownload > 120):
    velocidadeMinutos = velocidadeDownload / 60
    print(f"{int(velocidadeMinutos)} minutos")
else:
    print(f"{int(velocidadeDownload)} segundos")
