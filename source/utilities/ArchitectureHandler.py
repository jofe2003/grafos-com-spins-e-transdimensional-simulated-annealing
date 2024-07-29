import random
from source.utilities.WeightAdjuster import WeightAdjuster

class ArchitectureHandler:
# ////////////////////////////////////////////////////////////////////////////////// #
# /////////////////////////////////   DIVIDIR NEURONIO   /////////////////////////// #
# ////////////////////////////////////////////////////////////////////////////////// #
    def __init__(self):
        self.weightAdjuster = WeightAdjuster

    def divideWeights_jplus1(self, neurons:list)->list:
        """Divide um neurônio da camada j e um peso da camada j
        
        Returns: 
            list: lista de neurônios dividos e pesos modificados
        """
        # encontra os indices do neuronio e do peso a serem divididos
        indexNeuron, indexWeight = self.find_neuron_weight_layer_jplus1(neurons)

        # encontra o valor peso do peso a ser dividido
        weightToDivide = neurons[indexNeuron][indexWeight]

        # valores dos pesos após a divisão
        wLeft, wRight  = self.weightAdjuster.divide_weights_layer_jplus1(weightToDivide)

        neurons[indexNeuron][indexWeight] = wRight

        if indexWeight == 0:
            neurons.insert(indexNeuron, [wLeft])

        elif indexWeight == len(neurons[indexNeuron])-1:
            neurons[indexNeuron][indexWeight] = wLeft
            neurons.insert(indexNeuron + 1, [wRight])

        else:
            # copia a lista neurons[indexNeuron] a partir do elemento neurons[indexNeuron][indexWeight] a diante
            new_neuron = neurons[indexNeuron][-(len(neurons[indexNeuron]) - indexWeight):]
            neurons[indexNeuron][indexWeight] = wLeft
            del neurons[indexNeuron][indexWeight + 1:]

            if indexNeuron < len(neurons) - 1:
                neurons.insert(indexNeuron + 1, new_neuron)
            else:
                neurons.append(new_neuron)
        return neurons, indexNeuron

    def find_neuron_weight_layer_jplus1(self, neurons:list)->tuple:
        """Obtem dois índices, um do neurônio e outro de algum peso deste neurônio
        
        Returns:
            tuple: dois índices de um vetor
        """
        maxIndexNeurons = len(neurons)-1
        
        if maxIndexNeurons > 0: 
            indexNeuron = random.randint(0, maxIndexNeurons)
        else: # caso em que há somente um elo saindo do neurônio
            indexNeuron = maxIndexNeurons

        maxIndexWeight = len(neurons[indexNeuron])-1

        if maxIndexWeight > 0:
            indexWeight = random.randint(0, len(neurons[indexNeuron])-1)
        else:
            indexWeight = maxIndexWeight

        return indexNeuron, indexWeight
    
    def find_neuron_weight_layer_j(self, candidates:list)->tuple:
        """Obtem o indice do neurônio da camada j-1 e do seu respectivo peso para
        ser dividido
        
        Returns:
            tuple: dois inteiros, o índice do neurônio da camada j-1 e um peso seu respectivamente
        """
        maxIndex = len(candidates) - 1
        if maxIndex > 0:
            index = random.randint(0, maxIndex)
        else:
            index = maxIndex
        # print("aqui: ", candidates)
        # print("index: ", index)
        return candidates[index][0], candidates[index][1]

    def find_neuron_weight_possible2divide(self, neurons:list, indexNeuron:int)->tuple:
        """Obtém os possíveis pesos da camdada j-1 para serem divididos

        Returns:
            list: cada elemento é dois inteiros, o índice do neurônio e o índice do peso respectivamente
        """
        find = False
        found = False
        candidates = []
        k=0
        for neuron in range(len(neurons)):
            for weight in range(len(neurons[neuron])):
                candidate = [neuron, weight]
                k+=1
                if k == indexNeuron + 1:
                    find = True
                    found = True
                    candidates.append(candidate)
                else:
                    find = False
                if find == False and found == True:
                    break
            k-=1
            if find == False and found == True:
                break
        return self.find_neuron_weight_layer_j(candidates)

    def divideWeights_j(self, neurons:list, indexNeuron)->list:
        """ Divide algum peso do neurônio da camada j-1 que está conectado ao
        neurônio da camada j que foi dividido

        Returns:
            list: lista dos neurônios da camada j-1 com um peso dividido
        """
        searchNeuron, indexWeight = self.find_neuron_weight_possible2divide(neurons, indexNeuron)
        wLeft, WRight = self.weightAdjuster.divide_weights_layer_j(neurons[searchNeuron][indexWeight])
        neurons[searchNeuron][indexWeight] = WRight
        neurons[searchNeuron].insert(indexWeight, wLeft)

        return neurons

    def divideNeuron(self, layers:list)->list:
        """Recebe duas camadas de neurônios seguidas (camada j-1 e j) e, com isso
        realiza a divisão dos neurônios e seus respectivos pesos
        Returns:
            list: a lista das camadas j e j-1 modificadas
        """
        layers[1], indexNeuron = self.divideWeights_jplus1(layers[1])
        
        layers[0] = self.divideWeights_j(layers[0], indexNeuron)
        
        # return layers[0], layers[1]
        return layers

# ////////////////////////////////////////////////////////////////////////////////// #
# /////////////////////////////////   FUNDIR NEURONIO    /////////////////////////// #
# ////////////////////////////////////////////////////////////////////////////////// #
    def joinNeuron2Right_j(self, neurons:list, indexNeuron:int, indexWeight:int)->list:
        """Realiza a junção entre o peso de índice indexWeight e neurônio indexNeuron da camada j-1 
        com o peso imediatamente à direita

        Returns:
            list: lista dos neurônios já com os pesos fundidos à direita
        """

        wLeft = neurons[indexNeuron][indexWeight]
        wRight = neurons[indexNeuron][indexWeight+1]
        newW = self.weightAdjuster.join_weights_layer_j(wLeft, wRight)
        neurons[indexNeuron][indexWeight] = newW
        del neurons[indexNeuron][indexWeight+1]
        return neurons

    def findWeight2join_j(self, neurons:list, indexNeuron:int)->tuple:
        """Obtem os índices do neurônio da camada j-1 e do seu respectivo peso a ser fundido 
        com o peso imediatamente à direita

        Returns:
            tuple: índice do neurônio da camada j-1 e índice do peso respectivamente
        """
        find = False
        k=-1
        for neuron in range(len(neurons)):
            for weight in range(len(neurons[neuron])):
                k+=1
                if k == (indexNeuron+1) and not find:
                    find = True
                    break
                # print("(i, j), k, indexNeuron+1", neuron, weight, k, indexNeuron+1)
            if find:
                break
            k-=1
        return neuron, weight

    def joinNeuron2Right_jplus1(self, neurons:list, indexNeuron:int)->list:
        """Realiza a junção entre o último peso do neurônio indexNeuron da camada j 
        com o primeiro peso do neurônio de índice indexNeuron+1

        Returns:
            list: lista dos neurônios já com os neurônios fundidos à direita
        """
        lastWeight = len(neurons[indexNeuron])-1
        wLeft = neurons[indexNeuron][lastWeight]
        wRight = neurons[indexNeuron+1][0]
        newW = self.weightAdjuster.join_weights_layer_jplus1(wLeft, wRight)
        neurons[indexNeuron][lastWeight] = newW
        i = 1
        size = len(neurons[indexNeuron+1])
        while i < size:
            neurons[indexNeuron].append(neurons[indexNeuron+1][i])
            i+=1
        del neurons[indexNeuron+1]
        return neurons
    
    def joinNeuron2Left_jplus1(self, neurons:list, indexNeuron:int)->list:

        lastWeight = len(neurons[indexNeuron-1])-1
        wLeft = neurons[indexNeuron-1][lastWeight]
        wRight = neurons[indexNeuron][0]
        newW = self.weightAdjuster.join_weights_layer_jplus1(wLeft, wRight)
        neurons[indexNeuron][0] = newW
        i = 0
        size = len(neurons[indexNeuron-1])-1
        while i < size:
            neurons[indexNeuron].insert(i, neurons[indexNeuron-1][i])
            i+=1
        del neurons[indexNeuron-1]
        return neurons


    def find_neurons_possible2join(self, neurons:list)->list:
        """obtem o index de todos os nerônios que tem pelo menos um peso saido deste"""
        if len(neurons) > 1:
        # obtem o index de todos os nerônios que tem pelo menos um peso saido deste
            return [index for index, sublist in enumerate(neurons)]
        return []

    def chance_split2left(self):
        return random.uniform(0, 1)
    
    def find_neuron_2join(self, possibleNeurons:list)->int:
        """obtem um indice de um neurônio aleatóriamente"""
        indexNeuron = random.choice(possibleNeurons)
        return indexNeuron
    
    def joinNeurons_j(self, neurons:list, indexNeuron)->list:
        """Obtem a lista de neurônios da camada j-1 onde o neurônio indexNeuron foi fundido
        com o neurônio à direita
        """
        if indexNeuron != None:
            searchNeuron, indexWeight = self.findWeight2join_j(neurons, indexNeuron)
            neurons = self.joinNeuron2Right_j(neurons, searchNeuron, indexWeight-1)
        return neurons

    def joinNeurons_jplus1(self, neurons:list)->tuple:
        """Obtem a lista de neurônios da camada j com um neurônio fundido com o 
        seu vizinho à direita ou à esquerda a depender do índice
        Returns:
            tuple: lista de neurônios e o indice do neurônio que foi fundido à direita
        """
        indexNeuron = None
        # obtem o index de todos os nerônios que tem mais de um peso saido
        possibleNeurons = self.find_neurons_possible2join(neurons)
        if len(possibleNeurons) > 0:
            indexNeuron = self.find_neuron_2join(possibleNeurons)
            if indexNeuron == 0:
                neurons = self.joinNeuron2Right_jplus1(neurons, indexNeuron)
            elif indexNeuron == len(neurons)-1:
                neurons = self.joinNeuron2Left_jplus1(neurons, indexNeuron)
                indexNeuron = indexNeuron - 1
            else:
                if self.chance_split2left() < 0.50:
                    neurons = self.joinNeuron2Left_jplus1(neurons, indexNeuron)
                    indexNeuron = indexNeuron - 1
                else:
                    neurons = self.joinNeuron2Right_jplus1(neurons, indexNeuron)
        return neurons, indexNeuron

    def joinNeurons(self, layers:list)->list:
        """Recebe duas camadas de neurônios imediatamente seguidas e funde um
        neurônio da camada j e seu respectivo elo da camada j-1

        Returns:
            list: as duas camadas modificadas com seus respectivos neurônios e pesos
        """
        indexNeuron = None
        layers[1], indexNeuron = self. joinNeurons_jplus1(layers[1])
        layers[0] = self.joinNeurons_j(layers[0], indexNeuron)

        return layers
    



# v = [[1, 1, 1, 1], [1]]
# handler = ArchitectureHandler()
# print(v)
# v = handler.findWeight2join_j(v, 1)
# print(v)

    
#     def find_weight_2toin_jplus1(self, neurons):
#         maxIndex = len(neurons) - 1
#         if maxIndex > 0:
#             indexWeight = random.randint(0, maxIndex)
#         else:
#             indexWeight = maxIndex
#         return indexWeight
