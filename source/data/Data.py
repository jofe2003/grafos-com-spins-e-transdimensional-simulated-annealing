import csv
import numpy as np

class Data:
    def __init__(self, pontos, path, f):
        self.pontos = pontos
        self.path = path
        self.f = f
    
    def gerar_dados(self):
        # Gerando valores aleatórios para x e y
        x = np.random.uniform(low=-10, high=10, size=(self.pontos,))
        y = np.random.uniform(low=-10, high=10, size=(self.pontos,))
        z = np.random.uniform(low=-10, high=10, size=(self.pontos,))

        # Calculando z como a função que queremos aproximar: x + y + z + ruído pequeno
        noise = np.random.normal(loc=0, scale=0.1, size=(self.pontos,))

        result = self.f(x, y, z) + noise

        # Organizando os dados em uma lista de tuplas
        data = list(zip(x, y, z, result))

        self.save_data_csv(data)
        return

    def save_data_csv(self, data):
        
        # Escrevendo os dados em um arquivo CSV
        with open(self.path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['x', 'y', 'z', 'f'])  # Escreve o cabeçalho
            writer.writerows(data)  # Escreve os dados
        return