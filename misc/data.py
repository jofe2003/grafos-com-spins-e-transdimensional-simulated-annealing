import csv



def generate_points(): # gera os pontos da função

    points = []
    for x in range(-10, 11):
        for y in range(-10, 11):
            z = x + y
            points.append([x, y, z])
    return points

# Gerar pontos
points = generate_points()

# Salvar os pontos em um arquivo CSV
filename = "pontos.csv"
with open(filename, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y", "z"])  # Escreve o cabeçalho
    writer.writerows(points)

print(f"Pontos salvos no arquivo {filename}")




import csv
import os

def getData():
    # Lista para armazenar os pontos
    points = []

    # Caminho para o diretório onde está o arquivo CSV
    diretorio = ""
    # Nome do arquivo CSV
    nome_arquivo = "pontos.csv"
    # Caminho completo para o arquivo CSV
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)

    # Abrir o arquivo CSV
    with open(caminho_arquivo, "r", newline='') as f:
        reader = csv.reader(f)
        # Ler os dados do arquivo CSV
        for row in reader:
            points.append(row)
    return points
    # # Exibir os pontos lidos
    # for point in points:
    #     print(point)
print(getData)