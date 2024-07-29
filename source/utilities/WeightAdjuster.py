import numpy as np


class WeightAdjuster:

    def divide_weights_layer_jplus1(w):
        """Obtem o valor de cada peso da matriz j ao dividir-se um neurônio da camada j

        Returns:
            float: float com os novos pesos, esquerda e direita respectivamente
        """
        newR_w = np.random.normal((w)*0.5, 1) 
        newD_w = np.random.normal((w)*0.5, 1) 
        return newR_w, newD_w

    def divide_weights_layer_j(w)->float:
        """Obtem o valor de cada peso da matriz j-1 ao dividir-se um neurônio da camada j

        Returns:
            float: float com os novos pesos
        """
        newR_w = np.random.normal((w)*0.5, 1) 
        newD_w = np.random.normal((w)*0.5, 1) 
        return newR_w, newD_w

    def join_weights_layer_jplus1(w1, w2):
        """Obtem o valor do peso da matriz j ao fundir-se dois neurônios da camada j

        Returns:
            float: float com o novo peso
        """
        new_w = np.random.normal((w1 + w2), 1)
        return new_w
    
    def join_weights_layer_j(w1, w2):
        """Obtem o valor do peso da matriz j-1 ao fundir-se dois neurônios da camada j

        Returns:
            float: float com o novo peso
        """
        new_w = np.random.normal((w1 + w2), 1)
        return new_w