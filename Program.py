import random

from numpy import copy
from Model import Model
from source.data.Data import Data
import pandas as pd

from source.utilities.ActivateFunction import ActivateFunction

path = "C:\\Users\\meloja1\\OneDrive - Banco BTG Pactual S.A\\Desktop\\modelo\\model\\source\\data\\data.csv"

def findActivate(function):
    f = ActivateFunction()
    functions={
        "sigmoid":f.sigmoid,
        "relu":f.relu,
        "identity": f.identity
    }
    return functions[function]

def calculateF(modelo, rows):
    error = 0
    for row in rows:
        calculated = modelo.feedForward(row[:-1], 0)[0]
        error += (calculated-row[-1])**2

    return error

def expected(x, y, z):
    return x + y + z

def main():
    # # define os pontos
    # data = Data(1000, path, expected)
    # data.gerar_dados()

    # le os pontos
    df = pd.read_csv(path)
    rows = []
    for index, row in df.iterrows():
        x = row['x']
        y = row['y']
        z = row['z']
        f = row['f']
        rows.append((x, y, z, f))

    # define o modelo

    v3 = [[1],[1]]
    v2=[[1], [1,1]]
    v1 = [[1],[1,1],[1]]


    v=[v1,v2, v3]
    modelo_t = Model(v, 0.5, findActivate('relu')) # estrutura v, 0.5 a divisão para a esquerda, 'relu'

    # modelo_t2 = Model(v, 0.5, findActivate('sigmoid')) 
    # modelo_t2.change()
    modelo_t.toString()
    min_error = 10000
    for t in range(0,10000):
        t_error = calculateF(modelo_t, rows)

        if t_error < min_error:
            min_error = t_error

        modelo_tplus1 = modelo_t.copy()
        modelo_tplus1.change()
        tplus1_error = calculateF(modelo_tplus1, rows)
        print(tplus1_error)
        if tplus1_error < t_error:
            modelo_t = modelo_tplus1
            modelo_t.toString()

    modelo_t.toString()

    return 

main()