import copy
from source.utilities.ArchitectureHandler import ArchitectureHandler
from source.utilities.ActivateFunction import ActivateFunction
from source.utilities.Matriz import Matriz

import random

class Model:
    def __init__(self, architecture:list, rateArchitectural:float, activate):
        self.model = architecture
        self.rateArchitectural = rateArchitectural
        self.layers = len(architecture)
        self.handler = ArchitectureHandler()
        self.f = activate
        self.matriz = Matriz()

    def change(self):
        # if random.uniform(0,1) < self.rateArchitectural: # escolhe se vai mudar a arquitetura

            # escolhe um index possível de dividir ou juntar
        if self.layers > 2:
            index = random.randint(1, self.layers-1)
        else:
            index = self.layers - 1

        if random.uniform(0,1) <= .5: # divide
            print("DIVIDIU")
            self.model[index-1:index+1] = self.handler.divideNeuron(self.model[index-1:index+1])
        else:
            print("FUNDIU")
            self.model[index-1:index+1] = self.handler.joinNeurons(self.model[index-1:index+1])

        return 

    def toString(self):
        print("\nestrutura: ", self.model)

    def applyActivation(self, x):
        for i in range(len(x)):
            x[i] = self.f(x[i])
        return x

    def feedForward(self, input, index):
        if index == self.layers:
            return input
        y = self.matriz.dot(input, self.model[index])
        return self.feedForward(self.applyActivation(y), index + 1)
    
    def copy(self):
        return Model(copy.deepcopy(self.model), self.rateArchitectural, self.f)



# def main():
#     # v3 = [[1], [1], [1]]
#     # v2 = [[1,1],[1,1]]
#     # v1 = [[1], [1, 1], [1]]
#     # v = [v1, v2, v3]

#     v2=[[1], [1]]
#     v1 = [[1],[1,1],[1]]
#     v=[v1,v2]

#     model = Model(v, 0.5, 'relu')

#     model.change()

#     model.toString()

# main()